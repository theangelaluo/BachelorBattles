from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from form import PlayerForm, TurnForm, OpponentForm
from player import Player, Card, Move, makeCard, attack, checkDeck
from contestants import contestants, moves, dropdown

import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa68a37a2368cc3a03c3c0fc1079b8e2' #helps something about cookies

charList = list(contestants.keys())
user = Player("", [])
opponent = Player("Opponent", [makeCard("Kelsey"), makeCard("Lexi"), makeCard("Natasha"), makeCard("Mykenna")])

'''
while len(opponent.cards) < 4:
    index = random.randint(0, len(charList) - 1)
    elem = charList[index]
    if findElem(elem, opponent.cards) == None:
        opponent.cards.append(makeCard(elem))
'''


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
    show = 0
    form = TurnForm()
    opponentForm = OpponentForm()

    form.first.choices = dropdown([card.name for card in user.cards])
    form.second.choices = dropdown([card.name for card in opponent.cards])
    
    winner = endgame(opponent, user)
    if winner == opponent or winner == user:
        message = winner.name + " won!"
        show = 2
        return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
    
    if form.validate_on_submit():
        first = form.first.data
        second = form.second.data
        show = 1
        message = attack(user.name, findElem(first, user.cards), findElem(second, opponent.cards))
        updateList(opponent.cards)
        form.second.choices = dropdown([card.name for card in opponent.cards])
        return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
    
    if opponentForm.validate_on_submit():
        first = opponent.cards[random.randint(0, len(opponent.cards)-1)]
        second = user.cards[random.randint(0, len(user.cards)-1)]
        show = 0

        while second.hp <= 0 or first.hp <= 0:
            first = opponent.cards[random.randint(0, len(opponent.cards)-1)]
            second = user.cards[random.randint(0, len(user.cards)-1)]

        message = attack("Opponent", second, first)
        updateList(user.cards)
        form.first.choices = dropdown([card.name for card in user.cards])
        return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, message=message, opponentForm=opponentForm, show = show)
        
    return render_template('battle_room.html', deck = user.cards, name=user.name, opponentDeck = opponent.cards, form = form, opponentForm=opponentForm, message="It's your move! Select one of your cards to attack and one of your opponent's cards as the target.", show = show)


#finds a card in a list
def findElem(itemName, lst):
    for elem in lst:
        if elem.name == itemName:
            return elem
    return None

#removes cards
def updateList(lst):
    for card in lst:
        if card.hp <= 0:
            lst.remove(card)

#endgame
def endgame(opponent, player):
    if not checkDeck(opponent.cards):
        return player
    elif not checkDeck(player.cards):
        return opponent




if __name__ == "__main__":
    app.run()
