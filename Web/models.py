from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) 
    userName = db.Column(db.String(150), unique=False)
    password = db.Column(db.String(150))

class tempUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp_mail = db.Column(db.String(150), unique=True)
    temp_userName = db.Column(db.String(150), unique=False)
    temp_password = db.Column(db.String(150)) 

    def __init__(self, temp_mail, temp_userName, temp_password):
        self.temp_mail = temp_mail
        self.temp_userName = temp_userName
        self.temp_password = temp_password