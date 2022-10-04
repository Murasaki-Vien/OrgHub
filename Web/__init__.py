from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path




db = SQLAlchemy()
app = Flask(__name__)
db_Name = "OrgHub4254.db"


def createWebApp():
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "ASD234bjhgKGI"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_Name}'
    db.init_app(app)

    from Web.home.route import home
    from Web.forms.route import forms
    from Web.dashboard.route import Dashboard
    from Web.organizer.route import organizer
    from Web.profile.route import profile

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(forms, url_prefix="/")
    app.register_blueprint(Dashboard, url_prefix="/")
    app.register_blueprint(organizer, url_prefix="/")
    app.register_blueprint(profile, url_prefix="/")


    from Web.models import User, tempUser


    login_manager = LoginManager()
    login_manager.login_view = "forms.SignInPage"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('App/' + db_Name):
        db.create_all(app=app)