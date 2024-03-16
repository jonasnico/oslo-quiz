from flask import Blueprint, jsonify
from models.listing import Listing

listings = Blueprint('listings', __name__)

@listings.route('/api/listings', methods=['GET'])
def get_quizer():
    return jsonify([{'location': listing.location, 'venue': listing.venue, 'date': listing.date, 'time': listing.time, 'category': listing.category} for listing in Listing.query.all()])