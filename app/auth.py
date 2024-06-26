# save this as app.py
from flask import Blueprint, render_template, jsonify, current_app, redirect, url_for, request
from flask_login import login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # current_user.name
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        print(username, password, remember)
        # login user
        return redirect(url_for('hello', username=username), code=302)
    else:
        return render_template("login.html")

@auth.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('web.hello'))