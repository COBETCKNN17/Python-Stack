from flask import Flask 
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo(): 
    return "Dojo"

@app.route("/say/<name>/")
def say(name): 
    print(name)
    if(name=="flask"): 
        return "Hi Flask"
    else: 
        return "Hi "+name 
    
@app.route('/server/<name>/')
def server(name):
    print(name)
    return "server "+name 

@app.route("/repeat/<number>/hello")
def hello(number): 
    print_statement = ""
    for i in range(0,int(number)): 
        print_statement = print_statement + "<p>hello</h3><p>"
        print("hello")
    return print_statement

@app.route("/repeat/<number>/dogs")
def repeat(number): 
    print_statement = ""
    for i in range(0,int(number)): 
        print_statement = print_statement + "<h3>dog\r\n</h3><br>"
        print("dog")
    return print_statement
    #return ("dog was printed " + number + " of times" +"\r\n") * int(number)
    
if __name__=="__main__":
    app.run(debug=True)