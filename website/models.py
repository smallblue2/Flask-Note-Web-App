from website import DATABASE
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    data = DATABASE.Column(DATABASE.String(10000))
    date = DATABASE.Column(DATABASE.DateTime(timezone=True), default=func.now())
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('user.id'))

class User(DATABASE.Model, UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    email = DATABASE.Column(DATABASE.String(150), unique=True)
    password = DATABASE.Column(DATABASE.String(150))
    first_name = DATABASE.Column(DATABASE.String(150))
    notes = DATABASE.relationship('Note')