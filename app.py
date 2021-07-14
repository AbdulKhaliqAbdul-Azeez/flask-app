# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

 
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/results", methods = ["GET","POST"])
def results():
    user_choice_house = request.form["house"]
    user_choice_car = request.form["car"]
    user_choice_career = request.form["career"]
    user_choice_city = request.form["city"]
    return render_template("results.html", house = user_choice_house, car = user_choice_car, career = user_choice_career, city = user_choice_city)
