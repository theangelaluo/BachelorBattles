from flask import Flask, render_template, url_for, redirect
from form import PlayerForm
from player import Player, Card, Move, makeCard, dropdown, attack, checkDeck
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa68a37a2368cc3a03c3c0fc1079b8e2' #helps something about cookies
user = Player("", [])
opponent = Player("Opponent", [makeCard("Kelsey"), makeCard("Lexi"), makeCard("Natasha"), makeCard("Mykenna")])
opponentCharacters = dropdown([card.name for card in opponent.cards])

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

#char screen
@app.route("/char_select", methods = ['GET', 'POST'])
def char_select():
    form = PlayerForm()
    if form.validate_on_submit():
        user.cards.clear()
        user.name = form.name.data

        char1 = form.char1.data
        user.cards.append(makeCard(char1))

        char2 = form.char2.data
        user.cards.append(makeCard(char2))

        char3 = form.char3.data
        user.cards.append(makeCard(char3))

        char4 = form.char4.data
        user.cards.append(makeCard(char4))

        return redirect(url_for('battle_room'))
    return render_template('char_sel.html', form = form)

#battle room: at this point, user = [player's name, [list of cards in deck]]
@app.route("/battle_room", methods = ['GET', 'POST'])
def battle_room():
    from turnForm import TurnForm, OpponentForm
    show = 0
    form = TurnForm()
    opponentForm = OpponentForm()
    form.first.choices = dropdown([card.name for card in user.cards])
    winner = endgame(opponent, user)
    if winner == opponent or winner == user:
        message = winner.name + " won!"
        show = 2
        return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
    if form.validate_on_submit():
        first = form.first.data
        second = form.second.data
        if (findElem(second, opponent.cards)).hp <= 0:
            message = second + " is gone. Please Try again"
            return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
        else:
            show = 1
            message = attack(user.name, findElem(first, user.cards), findElem(second, opponent.cards))
            return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
    if opponentForm.validate_on_submit():
        first = user.cards[random.randint(0,3)]
        second = user.cards[random.randint(0,3)]
        show = 0
        while second.hp <= 0:
            second = user.cards[random.randint(0,3)]
        message = attack("Opponent", first, second)
        return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
    return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, opponentForm=opponentForm, message="It's your move! Select one of your cards to attack and one of your opponent's cards as the target.", show = show)



#endgame
def endgame(opponent, player):
    if not checkDeck(opponent.cards):
        return player
    elif not checkDeck(player.cards):
        return opponent

def findElem(itemName, lst):
    for elem in lst:
        if elem.name == itemName:
            return elem
    return None


if __name__ == "__main__":
    app.run()
