from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from player import dropdown


characters = dropdown()

class PlayerForm(FlaskForm):
    name = StringField('Player Name:', validators = [DataRequired(), Length(min = 2, max = 20)])
    char1 = SelectField('First Card:', validators = [DataRequired()], choices = characters)
    char2 = SelectField('Second Card:', validators = [DataRequired()], choices = characters)
    char3 = SelectField('Third Card:', validators = [DataRequired()], choices = characters)
    char4 = SelectField('Fourth Card:', validators = [DataRequired()], choices = characters)
    submit = SubmitField('Play')
