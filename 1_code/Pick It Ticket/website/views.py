# For other pages
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Room, Ticket, Seat
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import json


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/get-tickets')
@login_required
def get_tickets():
    rooms = Room.query.all()
    return render_template("get_tickets.html", user=current_user, rooms=rooms)


@views.route('/view-tickets')
@login_required
def view_tickets():
    return render_template("view_tickets.html", user=current_user)


@views.route('/set-tickets', methods=['GET', 'POST'])
@login_required
def set_tickets():
    if request.method == 'POST':
        name = request.form.get('roomName')
        show = request.form.get('show')
        rows = request.form.get('rows')
        columns = request.form.get('columns')
        mode = request.form.get('mode')
        day = request.form.get('day')
        month = request.form.get('month')
        cost = request.form.get('cost')

        if len(name) < 4:
            flash('Room Name must be greater than 3 characters.', category='error')
        elif len(rows) < 1:
            flash('Row count must be present.', category='error')
        elif len(columns) < 1:
            flash('Column count must be present.', category='error')
        elif len(cost) < 1:
            flash('Seat cost must be present.', category='error')
        else:
            capacity = int(rows) * int(columns)
            new_room = Room(name=name, show=show, rows=rows,
                            columns=columns, mode=mode, capacity=capacity, day=day, month=month, cost=cost)
            db.session.add(new_room)
            db.session.commit()
            counter = 0
            for row in range(new_room.rows):
                for column in range(new_room.columns):
                    new_seat = Seat(room_id=new_room.id, number=counter)
                    db.session.add(new_seat)
                    db.session.commit()
                    counter = counter + 1
                    print(Seat.query.get(1))

            flash('Room created successfully!', category='success')
            return redirect(url_for('views.get_tickets'))

    return render_template("set_tickets.html", user=current_user)


@views.route('/room/<string:id>')
def room(id):
    room = Room.query.get(id)
    seats = Seat.query.all()
    return render_template("room.html", user=current_user, room=room, seats=seats)


@views.route('/seat/<string:id>/<string:id2>')
def seat(id, id2):
    room = Room.query.get(id)
    seat = Seat.query.get(id2)
    return render_template("seat.html", user=current_user, room=room, seat=seat)


@views.route('/checkout/<string:id>/<string:id2>', methods=['GET', 'POST'])
def checkout(id, id2):
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        address = request.form.get('address')
        zip = request.form.get('zip')
        card = request.form.get('card')
        expM = request.form.get('month')
        expD = request.form.get('day')
        csc = request.form.get('code')

        if len(first_name) < 1:
            flash('Please enter your name.', category='error')
        elif len(last_name) < 1:
            flash('Please enter your name.', category='error')
        elif len(address) < 1:
            flash('Please enter your address.', category='error')
        elif len(zip) < 1:
            flash('Please enter your zip code.', category='error')
        elif len(card) < 1:
            flash('Please enter your credit card details.', category='error')
        elif len(csc) < 1:
            flash('Please enter your credit card details.', category='error')
        else:
            new_ticket = Ticket(
                seat_id=id2, user_id=current_user.id)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket purchased successfully!', category='success')
            return redirect(url_for('views.home'))
    room = Room.query.get(id)
    seat = Seat.query.get(id2)
    return render_template("checkout.html", user=current_user, room=room, seat=seat)
