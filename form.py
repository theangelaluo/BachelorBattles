from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from contestants import contestants, moves, dropdown

allCharacters = dropdown(contestants)

class PlayerForm(FlaskForm):
    name = StringField('Player Name:', validators = [DataRequired(), Length(min = 2, max = 20)])
    char1 = SelectField('First Card:', validators = [DataRequired()], choices = allCharacters)
    char2 = SelectField('Second Card:', validators = [DataRequired()], choices = allCharacters)
    char3 = SelectField('Third Card:', validators = [DataRequired()], choices = allCharacters)
    char4 = SelectField('Fourth Card:', validators = [DataRequired()], choices = allCharacters)
    submit = SubmitField('Play')

class TurnForm(FlaskForm):
    first = SelectField('Pick a Bachelorette:', validators = [DataRequired()])
    second = SelectField('Pick a Target:', validators = [DataRequired()])
    submit = SubmitField('Play Turn')


class OpponentForm(FlaskForm):
    submit = SubmitField("Opponent's Turn")

