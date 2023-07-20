from datetime import datetime
from app import db


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    reservation_date = db.Column(db.Date)
    reservation_time = db.Column(db.Time)
    num_guests = db.Column(db.Integer)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
