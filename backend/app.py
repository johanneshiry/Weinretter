from flask import Flask, request, jsonify
from flask_cors import CORS

from schematics.exceptions import DataError

from db import collection, passcode_collection
from telegram_bot import TelegramBot
from validation import validate_captcha
from schematics.models import Model
from schematics.types import StringType, FloatType, URLType, ListType, ModelType
from secrets import token_hex

app = Flask(__name__)
CORS(app)

content_bot = TelegramBot()


class LocationType(Model):
    lat = FloatType(required=True)
    lng = FloatType(required=True)


class AddressType(Model):
    housenumber = StringType(required=True, max_length=5)
    street = StringType(required=True)
    city = StringType(required=True)
    plz = StringType(required=True, min_length=4, max_length=5)


class CreateRestaurantRequest(Model):
    name = StringType(required=True)
    link = URLType(required=True)
    tags = ListType(StringType)
    telephone = StringType()
    description = StringType()
    captcha = StringType(required=True, validators=[validate_captcha])
    location = ModelType(LocationType, required=True)
    address = ModelType(AddressType, required=True)


@app.route('/api/restaurant', methods=['POST'])
def create_restaurant():
    try:
        r = CreateRestaurantRequest(request.get_json())
        r.validate()
    except DataError as e:
        return jsonify(e.to_primitive()), 400

    restaurant = {'link': r.link,
                  'name': r.name,
                  'location': (r.location.lng, r.location.lat),
                  'address': {
                      'housenumber': r.address.housenumber,
                      'street': r.address.street,
                      'plz': r.address.plz,
                      'city': r.address.city
                  },
                  'telephone': r.telephone,
                  'description': r.description,
                  'tags': r.tags}

    result = collection.insert_one(restaurant)
    rid = result.inserted_id
    passcode = token_hex(12)
    passcode_collection.insert_one({'restaurant_id': str(rid), 'passcode': passcode})

    try:
        content_bot.notify(rid=rid, name=r.name, link=r.link)
    except Exception as e:
        print(e)

    return jsonify({'restaurant_id': str(rid), 'passcode': passcode}), 201


@app.route('/api/restaurant')
def fetch_restaurants():
    try:
        left_lng = float(request.args.get('left_lng'))
        right_lng = float(request.args.get('right_lng'))
        bottom_lat = float(request.args.get('bottom_lat'))
        top_lat = float(request.args.get('top_lat'))
    except ValueError:
        return '', 400

    cursor = collection.find({
        '$and': [{
            'location': {
                '$within': {
                    '$box': [[left_lng, bottom_lat], [right_lng, top_lat]]
                }
            }
        }, {
            'blocked': {
                '$not': {'$eq': True}
            }
        }]
    })

    restaurants = [{'name': r['name'],
                    'link': r['link'],
                    'location': {'lat': r['location'][1], 'lng': r['location'][0]},
                    'address': r['address'],
                    'telephone': r.get('telephone'),
                    'description': r.get('description'),
                    'tags': r.get('tags')
                    } for r in cursor]
    return jsonify(restaurants)


if __name__ == '__main__':
    app.run()
