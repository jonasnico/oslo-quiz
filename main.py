import os
from db import db
from flask import Flask, jsonify, render_template
from scraper import get_data
from models.listing import Listing
from routes.listings import listings
from dotenv import load_dotenv
from google.cloud import secretmanager

load_dotenv()

app = Flask(__name__)

def access_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_id, version_id)
    try:
        response = client.access_secret_version(name)
        return response.payload.data.decode('UTF-8')
    except Exception as e:
        print(f"Error: {e}")
        print(f"Could not access secret: {name} in project: {project_id}")
        raise

if os.getenv('FLASK_ENV') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = access_secret_version('oslo-quiz', 'SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = access_secret_version('oslo-quiz', 'SQLALCHEMY_DATABASE_URI')
else:
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