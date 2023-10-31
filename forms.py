from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, StringField, SelectField, SubmitField

month_choices = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
]

class StoreIDForm(FlaskForm):
    store_id = IntegerField('Store ID', [validators.InputRequired()], render_kw={'placeholder': 'Store ID'})

class TenantForm(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    month_of_birth = SelectField('Month of Birth', choices=month_choices, validators = [validators.InputRequired()])
    day_of_birth = IntegerField('Day of Birth', [validators.InputRequired()])
    year_of_birth = IntegerField('Year of Birth', [validators.InputRequired()])
    street_address = StringField('Street Address', [validators.InputRequired()])
    city = StringField('City', [validators.InputRequired()])
    state = StringField('State', [validators.InputRequired()])
    zip = IntegerField('Zip Code', [validators.InputRequired()])
    phone_number = StringField('Phone Number', [validators.InputRequired()])
    
    submit = SubmitField('Rent Unit')
