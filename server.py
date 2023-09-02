"""Bleeze Server"""

from flask import Flask, render_template, session, redirect, request, url_for, flash
from jinja2 import StrictUndefined
from model import connect_to_db
from forms import StoreIDForm
import crud

app = Flask(__name__)
app.secret_key = "selfstorage"
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods = ["GET", "POST"])
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
    units = crud.get_units_by_store_id(store_id)


    return render_template("store.html", units = units)
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)