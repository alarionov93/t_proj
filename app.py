# save this as app.py
from flask import Flask, render_template, jsonify, current_app, redirect, url_for, request
from flask_login import login_required, current_user

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html", name='Alex', test='test')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        print(username, password, remember)
        # login user
        return redirect(url_for('hello'), code=302)
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)