from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from player import dropdown, contestants
from app import user, opponent


opponentCharacters = dropdown([card.name for card in opponent.cards])



class TurnForm(FlaskForm):
    first = SelectField('Pick a Bachelorette:', validators = [DataRequired()])
    second = SelectField('Pick a Target:', validators = [DataRequired()], choices = opponentCharacters)
    submit = SubmitField('Play Turn')


class OpponentForm(FlaskForm):
    submit = SubmitField("Opponent's Turn")
