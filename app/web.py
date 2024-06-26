from flask import Blueprint, render_template, current_app, redirect, url_for, request
from flask_login import login_required, current_user

web = Blueprint('web', __name__)

@web.route("/")
def hello():

    try:
        u = current_user.name
        email = current_user.email
    except AttributeError:
        u = None
        email = None
    return render_template("base.html", email=email, name=u)