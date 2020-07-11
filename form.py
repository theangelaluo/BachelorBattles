from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
     

characters = [('Jenn', 'jenn'), ('Test', 'test')]

class Player_Form(FlaskForm):
    name = StringField('Player Name', validators = [DataRequired(), Length(min = 2, max = 20)])
    char1 = SelectField('First Card', validators = [DataRequired()], choices = characters)
    submit = SubmitField('Play')