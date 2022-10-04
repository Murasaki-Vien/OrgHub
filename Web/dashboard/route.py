from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

Dashboard = Blueprint("Dashboard", __name__)

@Dashboard.route("/dashboard/<UserAcc>")
@login_required
def DashBoard(UserAcc):
    return render_template("dashboard.html", email=UserAcc)

