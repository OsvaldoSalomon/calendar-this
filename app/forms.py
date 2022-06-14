from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from datetime import datetime

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start", validators=[DataRequired(), ])
    start_time = TimeField("Start", validators=[DataRequired()])
    end_date = DateField("End", validators=[DataRequired()])
    end_time = TimeField("End", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private?")
    submit = SubmitField("Create Appointment")

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(field.data, form.end_time.data)
        start_date = form.start_date.data
        end_date = form.end_date.data
        if start >= end:
            msg = "End date/time must come after start date/time"
            raise ValidationError(msg)
        elif start_date != end_date:
            msg = "End date should be on the same day as the start date"
            raise ValidationError(msg)


