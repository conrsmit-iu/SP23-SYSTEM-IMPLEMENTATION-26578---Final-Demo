from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    tickets = db.relationship('Ticket')


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    show = db.Column(db.String(150))
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    rows = db.Column(db.Integer)
    columns = db.Column(db.Integer)
    mode = db.Column(db.String(15))
    cost = db.Column(db.String(15))
    seat = db.relationship('Seat')


class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occupied = db.Column(db.Boolean, default=False)
    number = db.Column(db.Integer)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    ticket = db.relationship('Ticket')


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'))
