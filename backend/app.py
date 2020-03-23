from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse
import requests
from db import collection
from content_control import TelegramBot

app = Flask(__name__)
CORS(app)

content_bot = TelegramBot()


def verify_captcha(token):
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      {'response': token, 'secret': '6Le3Kp4UAAAAAMkPcidI-o8gDu807ZnqzLr9Axqb'})
    return r.json()["success"]


@app.route('/api/restaurant', methods=['POST'])
def create_restaurant():
    body = request.get_json()

    link = body['link']
    address = body.get('address')
    description = body.get('description')
    tags = body.get('tags')
    telephone = body.get('telephone')

    if not verify_captcha(body['captcha']):
        return '', 403

    # XXX URL Validation
    # try:
    #    urlparse(link)
    # except:
    #    return '', 400

    name = body['name']
    location = (float(body['location']['lng']), float(body['location']['lat']))

    restaurant = {'link': link,
                  'name': name,
                  'location': location,
                  'address': address,
                  'telephone': telephone,
                  'description': description,
                  'tags': tags}

    result = collection.insert_one(restaurant)

    try:
        content_bot.notify(restaurant, result.inserted_id)
    except Exception as e:
        print(e)

    return '', 204


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
