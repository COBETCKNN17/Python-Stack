from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", box=1)

@app.route('/play/<box>/<color>/')
def show_boxes(box, color):
    return render_template("index.html", box=int(box), color=color)

if __name__=="__main__":
    app.run(debug=True)

