import os
from db import db
from flask import Flask, jsonify, render_template
from scraper import get_data
from models.listing import Listing
from routes.listings import listings
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.register_blueprint(listings)

db.init_app(app)

def update_listings():
    listings = get_data()
    for listing in listings:
        new_listing = Listing(location=listing['location'], venue=listing['venue'], date=listing['date'], time=listing['time'], category=listing['category'])
        db.session.add(new_listing)
    db.session.commit()

@app.route('/api/listings', methods=['GET'])
def get_listings():
    return jsonify(get_data())

@app.route("/")
def homepage():
    return render_template("liste.html", title="HOME PAGE")

@app.route("/liste")
def liste():
    return render_template("liste.html", title="LISTE")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        update_listings()
    app.run(debug=True)