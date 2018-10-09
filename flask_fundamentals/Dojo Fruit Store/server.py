from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def entername():
	return render_template('index.html')

@app.route('/purchase', methods=['POST'])
def purchase():
    print(request.form)
    name = request.form['name']
    s_quantity = request.form['s_quantity']
    r_quantity = request.form['r_quantity']
    b_quantity = request.form['b_quantity']
    item_quantity = int(s_quantity) + int(r_quantity) + int(b_quantity)
    student_id = request.form['student_id']
    created_date = datetime.datetime.today().strftime('%Y-%m-%d')
    return render_template('/purchase.html', name=name, s_quantity=s_quantity, r_quantity=r_quantity, b_quantity=b_quantity, item_quantity= item_quantity, student_id=student_id, created_date=created_date )

@app.route('/reset', methods=['GET', 'POST'])
def reset_session(): 
	return render_template('index.html')

if __name__=="__main__":  
    app.run(debug=True)