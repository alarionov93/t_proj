from flask import Blueprint, render_template, current_app, redirect, url_for, request
from flask_login import login_required, current_user

web = Blueprint('web', __name__)

@web.route("/")
def hello():
    return render_template("base.html", name='Alex')