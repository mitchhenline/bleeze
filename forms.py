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

day_choices = [
    ('01', '1'),
    ('02', '2'),
    ('03', '3'),
    ('04', '4'),
    ('05', '5'),
    ('06', '6'),
    ('07', '7'),
    ('08', '8'),
    ('09', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31')
]


class StoreIDForm(FlaskForm):
    store_id = IntegerField('Store ID', [validators.InputRequired()], render_kw={'placeholder': 'Store ID'})

class TenantForm(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    month_of_birth = SelectField('Month of Birth', choices=month_choices, validators = [validators.InputRequired()])
    day_of_birth = SelectField('Day of Birth', choices=day_choices, validators = [validators.InputRequired()])
    year_of_birth = IntegerField('Year', [validators.InputRequired()])
    # street_address = StringField('Street Address', [validators.InputRequired()])
    # city = StringField('City', [validators.InputRequired()])
    # state = StringField('State', [validators.InputRequired()])
    # zip = IntegerField('Zip Code', [validators.InputRequired()])
    # phone_number = StringField('Phone Number', [validators.InputRequired()])
    
    submit = SubmitField('Rent Unit')
