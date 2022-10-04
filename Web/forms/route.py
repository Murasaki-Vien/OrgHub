from flask import Blueprint, render_template, redirect, url_for, request, flash
import email
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from Web.models import User, tempUser
from Web import db, app
from flask_mail import Message, Mail
import random


forms = Blueprint("forms", __name__)
number = random.randint(1111,9999)

app.config['DEBUG'] = True
app.config['Testing'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['SECRET_KEY'] = "SADFNLIKRFNOERN"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'officialorghub@gmail.com'
app.config['MAIL_PASSWORD'] = 'tgifzzumvviplxkd'

mail = Mail(app)



@forms.route("/sign-in", methods = ['GET', 'POST'])
def SignInPage():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if email != "":
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in Successfully", category='success')
                    login_user(user)
                    return redirect(url_for("Dashboard.DashBoard", UserAcc=current_user.userName))
                else:
                    flash("Incorrect password", category="error")  
            else:
                flash("Email does not exist.", category='error')  

    return render_template("signin.html")

@forms.route("/sign-up", methods=['GET','POST'])
def SignUpPage():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            # if user already exists prompt error
            flash("User already exists.")
        
        elif len(username) < 5 or username == "":
            # if username is not valid prompt error
            flash("Invalid username.")

        elif len(email) < 5 or email == "":
            # if email is not valid prompt error
            flash("Invalid email.")

        elif len(password) < 4 or password == "":
            # if password is not valid prompt error
            flash("Invalid password.")
        
        else:
            num = str(number)

            temp_new_user = tempUser(temp_mail=email, temp_userName=username, temp_password=generate_password_hash(password, method='sha256'))

            db.session.add(temp_new_user)
            db.session.commit()

            msg = Message("Your Verification Code is: " + num, sender='officialorghub@gmail.com', recipients=[email])
            mail.send(msg)
            
            return redirect(url_for("forms.verify", user_id=temp_new_user.id))

            
    return render_template("signup.html")

@forms.route("/log-out")
@login_required
def LogoutPage():
    
    return redirect(url_for("home.LandingPage"))


@forms.route("/sign-up/verification/<int:user_id>", methods=['GET','POST'])
def verify(user_id):

    if request.method == 'POST':
        verifyCode= request.form.get("value")
        val = int(verifyCode)

        if val == number:
            tempuser = tempUser.query.filter_by(id=user_id).first()


            user = User(email=tempuser.temp_mail, userName=tempuser.temp_userName, password=tempuser.temp_password)

            g_email = tempuser.temp_mail

            db.session.add(user)
            db.session.delete(tempuser)
            db.session.commit()
            
            user = User.query.filter_by(email=g_email).first()

            login_user(user)
            flash('Account created')
            return redirect(url_for("Dashboard.DashBoard", UserAcc=current_user.userName))
        else:
            flash("Incorrect Code type again.")
            

    return render_template("verification.html", userID = user_id)



