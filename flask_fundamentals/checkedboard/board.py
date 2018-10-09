from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    list = [
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1]
    ]
    str = ""
    for i in list:
        str+="<div>"
        for j in i:
            str += "<div class='box'"
            if j == 1:
                str+="style='background-color:red'"
            if j == 2:
                str+="style='background-color:black'"
            str+=">hello</div>"
        str+="</div>"
    return render_template("index.html",context=str)

@app.route('/<x>/<y>')
def newboard(x):
    newtle = []
    for i in range(1,x):
        if(i%2==0):
            i = 2
            row.append(i)
        else:
            i = 1
            row.append(i)




if __name__=="__main__":
    app.run(debug=True)
