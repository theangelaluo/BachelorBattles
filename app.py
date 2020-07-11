from flask import Flask, render_template, url_for, redirect
from form import Player_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa68a37a2368cc3a03c3c0fc1079b8e2' #helps something about cookies


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html') #picture won't load on my end for some reason

#TODO char screen
@app.route("/char_select")
def char_select():
    form = Player_Form()

    return render_template('char_sel.html', form = form)

#TODO battle room
@app.route("/battle_room")
def battle_room():
    return render_template('battle_room.html')

if __name__ == "__main__":
    app.run()
