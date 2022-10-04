from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from Web.models import User, tempUser

organizer = Blueprint("organizer", __name__)

@organizer.route("/organizer")

def Organizer():

    return render_template("organizer.html")
