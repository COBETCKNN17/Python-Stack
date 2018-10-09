from flask import Flask, render_template, request, session, redirect 
import random 
from datetime import datetime, date, time 

app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    if (session.get('gold') is None):
        session['gold'] = 0
    if (session.get('activity') is None):
        session['activity'] = ""
    return render_template('index.html', activity = session['activity'])

@app.route('/process_money', methods=['POST'])
def process(): 
    building = request.form['building']
    message = "" 
    if request.form['building'] == 'farm': 
        result = random.randrange(10,21)
        session["gold"] += result 
        message = "You earned " + str(result) + " gold coins on the farm!<br>" 
    elif request.form['building'] == 'cave': 
        result = random.randrange(10,21)
        session["gold"] += result 
        message = "You earned " + str(result) + " gold coins in the cave!<br>" 
    elif request.form['building'] == 'house': 
        result = random.randrange(2,5)
        session["gold"] += result 
        message = "You earned " + str(result) + " gold coins in the house!<br>" 
    elif request.form['building'] == 'casino': 
        result = random.randrange(-50,50)
        session["gold"] += result 
        if result > 0: 
            message = "You earned " + str(result) + " gold coins in the casino!<br>" 
        elif result == 0: 
            message = "You broke even at the Casino!" 
        else: 
            message = "You lost " + str(result) + " gold coins in the casino!<br>" 
    session['activity'] += message
    return redirect ('/')

@app.route('/reset')
def reset():
    session['gold']=0
    session['activity'] = ""
    return redirect('/')

app.run(debug=True)