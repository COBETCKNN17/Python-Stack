from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = (
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'age' : 35},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'age' : 30},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age' : 25},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age' : 20}
    )

    length = len(users)

    return render_template("index.html", users=users, length=length)

if __name__=="__main__":
    app.run(debug=True)

