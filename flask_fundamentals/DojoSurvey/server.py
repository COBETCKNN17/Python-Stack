from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def entername():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print("in progress")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    description = request.form['description']
    return render_template('/result.html', name=name, location=location, language=language, description=description )
	# return redirect('/result') #never render post

@app.route('/reset', methods=['GET', 'POST'])
def reset_session(): 
	return render_template('index.html')

app.run(debug=True)