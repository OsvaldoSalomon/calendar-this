from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)

validatorRequired = [DataRequired()]

class AppointmentForm(FlaskForm):
    name = StringField("Name", validatorRequired)
    start_date = DateField("Start", validatorRequired)
    start_time = TimeField("Start", validatorRequired)
    end_date = DateField("End", validatorRequired)
    end_time = TimeField("End", validatorRequired)
    description = TextAreaField("Description", validatorRequired)
    private = BooleanField("Private?")
    submit = SubmitField("Create Appointment")


