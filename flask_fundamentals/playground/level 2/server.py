from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", box=0)
if __name__=="__main__":
    app.run(debug=True)

@app.route('/play/')
def show_boxes(box):
    return render_template("index.html")