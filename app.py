# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html", name='Alex', test='test')

@app.route("/books")
def books():
    return ['asdfg']

if __name__ == '__main__':
    app.run(debug=True)