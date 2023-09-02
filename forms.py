from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class StoreIDForm(FlaskForm):
    store_id = IntegerField('Store ID ', [validators.InputRequired()])
