from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db' # you can change this to postgresql once you have a server and db on it.
    app.secret_key = 'Some Key' # Change when deploying

    db.init_app(app)

    from models import user

    login_manager = LoginManager(app)    
    @login_manager.user_loader
    def load_user(uid):
        return user.query.get(uid)

    encrypt = Bcrypt(app)

    #import later
    from routes import register_routes
    register_routes(app, db, Bcrypt)

    migrate = Migrate(app, db)

    return app