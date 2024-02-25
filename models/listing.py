from db import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), nullable=False)
    venue = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)

    def __init__(self, location, venue, date, time, category):
        self.location = location
        self.venue = venue
        self.date = date
        self.time = time
        self.category = category