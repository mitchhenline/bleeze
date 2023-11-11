"""Bleeze Server"""

from flask import Flask, render_template, session, redirect, request, url_for, flash
from jinja2 import StrictUndefined
from model import connect_to_db, db, Renter
from forms import StoreIDForm, TenantForm
import crud

app = Flask(__name__)
app.secret_key = "selfstorage"
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods=["GET", "POST"])
def store_select():
    """View store selector."""
    form = StoreIDForm(request.form)

    if form.validate_on_submit():
        store_id = form.store_id.data

        if crud.is_valid_store(store_id):
            session['store_id'] = store_id
            return redirect(url_for('view_store', store_id=store_id))

        else:
            flash("Invalid store number. Please try again.")

    return render_template("store_selector.html", form=form)

@app.route('/<int:store_id>')
def view_store(store_id):
    """View store."""
    all_units = crud.get_units_by_store_id(store_id)
    store = crud.get_store_by_id(store_id)

    units = sorted(all_units, key=lambda unit: (unit.unit_number, unit.unit_number))

    return render_template("store.html", units = units, store = store)


@app.route('/<int:store_id>/unit/<int:unit_id>')
def view_unit(store_id, unit_id):
    """View unit details and handle unit renting."""
    unit = crud.get_unit_by_id(unit_id)
    store = crud.get_store_by_id(store_id)

    form = TenantForm(request.form)

    return render_template("unit.html", unit=unit, store=store, form=form)

@app.route('/<int:store_id>/unit/<int:unit_id>', methods = ['POST', 'PUT'])
def rent_unit(store_id, unit_id):
    """rent unit"""
    unit = crud.get_unit_by_id(unit_id)
    store = crud.get_store_by_id(store_id)
    form = TenantForm(request.form)
    if form.validate_on_submit():
        new_tenant = Renter(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            month_of_birth=form.month_of_birth.data,
            day_of_birth=form.day_of_birth.data,
            year_of_birth=form.year_of_birth.data,
            street_address=form.street_address.data,
            city=form.city.data,
            state=form.state.data,
            zip=form.zip.data,
            phone_number=form.phone_number.data,
        )

        db.session.add(new_tenant)
        db.session.commit()

        unit.rented = True
        unit.renter_id = new_tenant.id
        db.session.commit()
        flash("Unit rented successfully.")
        return redirect(request.url)

    else:
        flash("Error reserving unit")
        return redirect(request.url)

    

@app.route('/retail/<int:store_id>')
def view_store_retail(store_id):
    """View store retail."""
    retail = crud.get_retail_by_store_id(store_id)
    store = crud.get_store_by_id(store_id)

    return render_template("retail.html", retail=retail, store=store)

@app.route('/retail_unit/<int:store_id>/unit/<int:unit_id>')
def view_retail_unit(store_id, unit_id):
    """View unit details for retail units."""
    unit = crud.get_unit_by_id(unit_id)
    store = crud.get_store_by_id(store_id)

    return render_template("unit.html", unit=unit, store=store)

@app.route('/renter/<int:renter_id>')
def view_renter(renter_id):
    """View tenant details."""
    renter = crud.get_renter_by_id(renter_id)
    units = crud.get_units_by_renter_id(renter_id)

    return render_template("renter.html", renter=renter, units=units)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
