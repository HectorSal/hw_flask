from app import myapp_obj
from flask import render_template, flash, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    user_input = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        flash(request.form.get("user_input"))
    return render_template('home.html', name = name, city_names = city_names, form = form)
