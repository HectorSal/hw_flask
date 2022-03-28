from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputForm(FlaskForm):
    city_name = StringField('City Name')
    submit = SubmitField('Submit')
