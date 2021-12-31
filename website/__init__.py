from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


DATABASE = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AewTqGF2daf!3gea3$2GEA_g3q2qEFAWe2"$%^&erga32q32GrgFHtrrxhFt4wAYt5yu^fyNGfxdzgrA3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % (DB_NAME)
    DATABASE.init_app(app)

    from website.views import views
    from website.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from website.models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        DATABASE.create_all(app=app)
        print('Created Database!')