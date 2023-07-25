from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, DecimalField, HiddenField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class EditForm(FlaskForm):
    id = HiddenField('ID')  # Add a hidden field to store the item's ID
    mnozstvi = StringField('Množství', validators=[DataRequired()])
    jidlo = StringField('Jídlo', validators=[DataRequired()])
    alergeny = StringField('Alergeny', validators=[DataRequired()])
    cena = StringField('Cena', validators=[DataRequired()])

    class Meta:
        csrf = False
