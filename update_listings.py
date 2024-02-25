from scraper import get_data
from db import db, Listing

def update_listings():
    listings = get_data()
    for listing in listings:
        new_listing = Listing(location=listing['location'], venue=listing['venue'], date=listing['date'], time=listing['time'], category=listing['category'])
        db.session.add(new_listing)
    db.session.commit()

if __name__ == '__main__':
    update_listings()