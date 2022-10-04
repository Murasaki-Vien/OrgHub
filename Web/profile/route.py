import profile
from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from Web.models import User, tempUser

profile = Blueprint("profile", __name__)

@profile.route("/profile")

def Profile():

    return render_template("profile.html")
