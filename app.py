from flask import Flask, render_template, url_for, redirect
from form import PlayerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa68a37a2368cc3a03c3c0fc1079b8e2' #helps something about cookies


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html') 

#char screen
@app.route("/char_select", methods = ['GET', 'POST'])
def char_select():
    form = PlayerForm()
    if form.validate_on_submit():
        return redirect(url_for('battle_room'))
    return render_template('char_sel.html', form = form)

#battle room
@app.route("/battle_room")
def battle_room():
    return render_template('battle_room.html')




if __name__ == "__main__":
    app.run()
