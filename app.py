from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html') #picture won't load on my end for some reason

#TODO char screen
@app.route("/char_select")
def char_select():
    return render_template('char_sel.html')

#TODO battle room
