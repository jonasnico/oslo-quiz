from flask import Flask, jsonify, render_template

from scraper import get_data

app = Flask(__name__)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    return jsonify(get_data())

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/liste")
def liste():
    return render_template("liste.html", title="LISTE")

if __name__ == '__main__':
    app.run(debug=True)