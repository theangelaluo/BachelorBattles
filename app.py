from flask import Flask, render_template, url_for, redirect
from form import PlayerForm
from player import Player, Card, Move, makeCard

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa68a37a2368cc3a03c3c0fc1079b8e2' #helps something about cookies
user = Player("", []) 


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html') 

#char screen
@app.route("/char_select", methods = ['GET', 'POST'])
def char_select():
    form = PlayerForm()
    if form.validate_on_submit():
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
@app.route("/battle_room")
def battle_room():
    return render_template('battle_room.html', deck = user.cards)




if __name__ == "__main__":
    app.run()
