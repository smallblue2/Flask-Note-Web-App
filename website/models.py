from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Note model
class Note(db.Model):
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # Text content
    data = db.Column(db.String(10000))
    # Date created
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Foreign key to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# User model
class User(db.Model, UserMixin):
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # Email field
    email = db.Column(db.String(150), unique=True)
    # password field
    password = db.Column(db.String(150))
    # first name field
    first_name = db.Column(db.String(150))
    # one to many relationship
    notes = db.relationship('Note')
