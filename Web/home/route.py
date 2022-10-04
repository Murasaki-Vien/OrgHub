from flask import Blueprint, render_template, redirect

home = Blueprint('home', __name__)


@home.route("/")
def LandingPage():

    return render_template("index.html")

