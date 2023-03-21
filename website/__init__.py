# Import required libraries and modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the database object
db = SQLAlchemy()
# Set the database name
DB_NAME = 'database.db'


# Function to create the Flask app and configure it
def create_app():
    # Create the Flask app object
    app = Flask(__name__)
    # Set the app secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = 'AewTqGF2daf!3gea3$2GEA_g3q2qEFAWe2"$%^&erga32q32GrgFHtrrxhFt4wAYt5yu^fyNGfxdzgrA3'
    # Set the app SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # Initialize the app with the database object
    db.init_app(app)

    # Import the views and auth blueprints.
    from website.views import views
    from website.auth import auth
    
    # Register the blueprints with the app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the User and Note models
    from website.models import User, Note

    # Create the database tables within the app context
    # Safe to use, only creates tables if they don't exist
    with app.app_context():
        db.create_all()

    # Initialize the login manager
    login_manager = LoginManager()
    # Set the login view for redirecting unauthenticated users
    login_manager.login_view = 'auth.login'
    # Initialize the app with the login manager
    login_manager.init_app(app)

    # Define the user_loader function for retrieving user by ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Return the app object
    return app
