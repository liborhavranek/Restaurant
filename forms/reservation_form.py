from flask_wtf import FlaskForm
from wtforms import DateField, TimeField, IntegerField, StringField
from wtforms.validators import DataRequired, Email, Length


class ReservationForm(FlaskForm):
    reservation_date = DateField('Datum rezervace', validators=[DataRequired()])
    reservation_time = TimeField('Čas rezervace', validators=[DataRequired()])
    num_guests = IntegerField('Počet hostů', validators=[DataRequired()])
    name = StringField('Jméno', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    phone = StringField('Telefon', validators=[DataRequired(), Length(max=20)])
