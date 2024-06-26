# save this as app.py
from flask import Blueprint, render_template, jsonify, current_app, redirect, url_for, request, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # current_user.name
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        print(email, password, remember)
        # login user
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)

        return redirect(url_for('web.hello', email=email), code=302)
    else:
        try:
            whoami = current_user.name
        except AttributeError:
            whoami = None
        return render_template("login.html", whoami=whoami)

@auth.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('web.hello'))