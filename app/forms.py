from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from app.board import Color

COLOR_CHOICES = [(c.value, c.value) for c in Color if c != Color.WHITE]

class PlayerSetupForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    color = SelectField('Color', choices=COLOR_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Play')