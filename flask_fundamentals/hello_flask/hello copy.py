from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/coding")
def coding():
    return "<h1>Coding Dojo</h1>"

@app.route('/success')
def success():
    print("hello success")
    return "success"
@app.route('/server/<name>/')
def server(name):
    print(name)
    return "server "+name 
    
@app.route('/users/<username>/<id>')
def show_user_profile(username, id): 
    print(username)
    print(id)
    return "username : " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)

