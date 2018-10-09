from flask import Flask, flash, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'secret'

def createSession():
	session['num'] = random.randint(1,101)
	session['message'] = ''

@app.route('/')
def index(): 
	if 'message' not in session: 
		session['message'] =""
	else: 
		pass 
	print(session['num'])
	return render_template('index.html', message=session['message'])

@app.route('/guess', methods=['POST'])	
def guess_the_number(): 
	error = None 
	success = None 
	user_guess = request.form['guess']
	if request.method == 'POST': 
		if user_guess.isdigit(): 
			number_guess = int(user_guess)
			if number_guess == session['num']: 
				session['message'] = "You guessed the correct number!"
				#flash('Correct!', 'success')	# similar to alert in javascript 
				return redirect('/')
			elif number_guess > session['num']: 
				session['message'] = "You guessed too high"
				#flash('You guessed too high', 'error')
				return redirect('/')
			else: 
				session['message'] = "You guessed too low"
				#flash('You guessed too low', 'error')
		else: 
			session['message'] = "Not a number. Please enter a number."
			#flash('Not a number. Please enter a number')
		return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset_session(): 
	createSession()
	session.pop("message")
	return redirect('/')
	
app.run(debug=True)