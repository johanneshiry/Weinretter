from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient, GEOSPHERE
from urllib.parse import urlparse
from captcha import verify_captcha
from content_control import TelegramBot

client = MongoClient('localhost', 27017)
db = client.weinretter
collection = db.restaurants
collection.create_index([('location', GEOSPHERE)])

app = Flask(__name__)
CORS(app)

content_bot = TelegramBot()

@app.route('/api/restaurant', methods=['POST'])
def create_restaurant():
    body = request.get_json()

    link = body['link']
    address = body.get('address')
    description = body.get('description')
    # XXX URL Validation
    try:
        urlparse(link)
    except:
        return '', 400

    if not verify_captcha(body['captcha']):
        return '', 403

    name = body['name']
    location = (body['location']['lng'], body['location']['lat'])

    restaurant = {'link': link, 'name': name, 'location': location, 'address': address, 'description': description}

    content_bot.notify(restaurant)

    collection.insert(restaurant)

    return '', 204

@app.route('/api/restaurant')
def fetch_restaurants():
    left_lng = float(request.args.get('left_lng'))
    right_lng = float(request.args.get('right_lng'))
    bottom_lat = float(request.args.get('bottom_lat'))
    top_lat = float(request.args.get('top_lat'))

    cursor = collection.find({'location': {'$within': {'$box': [[left_lng, bottom_lat], [right_lng, top_lat]]}}})

    restaurants = [{'name': r['name'],
                    'link': r['link'],
                    'location': {'lat': r['location'][1], 'lng': r['location'][0]},
                    'address': r['address'],
                    'description': r['description']} for r in cursor]
    return jsonify(restaurants)
