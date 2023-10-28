from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, StringField, SelectField, SubmitField

class StoreIDForm(FlaskForm):
    store_id = IntegerField('Store ID', [validators.InputRequired()], render_kw={'placeholder': 'Store ID'})

class TenantForm(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    month_of_birth = IntegerField('Month of Birth', [validators.InputRequired()])
    day_of_birth = IntegerField('Day of Birth', [validators.InputRequired()])
    year_of_birth = IntegerField('Year of Birth', [validators.InputRequired()])
    street_address = StringField('Street Address', [validators.InputRequired()])
    city = StringField('City', [validators.InputRequired()])
    state = StringField('State', [validators.InputRequired()])
    zip = IntegerField('Zip Code', [validators.InputRequired()])
    phone_number = StringField('Phone Number', [validators.InputRequired()])
    
    submit = SubmitField('Rent Unit')
