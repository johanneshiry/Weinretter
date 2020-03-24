from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.objectid import ObjectId
from db import collection, passcode_collection
from telegram_bot import TelegramBot
from validation import validate_captcha
from schematics.models import Model
from schematics.types import StringType, FloatType, URLType, ListType, ModelType
from schematics.exceptions import DataError

from secrets import token_hex

app = Flask(__name__)
CORS(app)

content_bot = TelegramBot()


class LocationType(Model):
    lat = FloatType(required=True)
    lng = FloatType(required=True)

    def to_document(self):
        return (self.lng, self.lat)

    @staticmethod
    def from_document(doc):
        loc = LocationType()
        loc.lng = doc[0]
        loc.lat = doc[1]
        return loc


class AddressType(Model):
    housenumber = StringType(required=True, max_length=5)
    street = StringType(required=True)
    city = StringType(required=True)
    plz = StringType(required=True, min_length=4, max_length=5)

    def to_document(self):
        return {
            "housenumber": self.housenumber,
            "street": self.street,
            "plz": self.plz,
            "city": self.city,
        }

    @staticmethod
    def from_document(doc):
        return AddressType(doc)


class RestaurantModel(Model):
    id = StringType()
    name = StringType(required=True)
    link = URLType(required=True)
    tags = ListType(StringType)
    telephone = StringType()
    description = StringType()
    location = ModelType(LocationType, required=True)
    address = ModelType(AddressType, required=True)

    def to_document(r):
        return {
            "name": r.name,
            "link": r.link,
            "location": r.location.to_document(),
            "address": r.address.to_document(),
            "telephone": r.telephone,
            "description": r.description,
            "tags": r.tags,
        }

    @staticmethod
    def from_document(doc):
        r = RestaurantModel()
        r.name = doc.get("name")
        r.link = doc.get("link")
        r.location = LocationType.from_document(doc.get("location"))
        r.address = AddressType.from_document(doc.get("address"))
        r.description = doc.get("description")
        r.tags = doc.get("tags")
        return r


class CreateRestaurantModel(RestaurantModel):
    captcha = StringType(required=True, validators=[validate_captcha])


@app.route("/api/restaurants", methods=["POST"])
def create_restaurant():
    try:
        r = CreateRestaurantModel(request.get_json())
        r.validate()
    except DataError as e:
        return jsonify(e.to_primitive()), 400

    passcode = token_hex(12)

    doc = r.to_document()
    # store passcode "out-of-band"
    doc['passcode'] = passcode
    result = collection.insert_one(doc)

    rid = result.inserted_id

    try:
        content_bot.notify(rid=rid, name=r.name, link=r.link)
    except Exception as e:
        print(e)

    return jsonify({"restaurant_id": str(rid), "passcode": passcode}), 201


@app.route("/api/restaurants")
def fetch_restaurants():
    try:
        left_lng = float(request.args.get("left_lng"))
        right_lng = float(request.args.get("right_lng"))
        bottom_lat = float(request.args.get("bottom_lat"))
        top_lat = float(request.args.get("top_lat"))
    except ValueError:
        return "", 400

    cursor = collection.find(
        {
            "$and": [
                {
                    "location": {
                        "$within": {
                            "$box": [[left_lng, bottom_lat], [right_lng, top_lat]]
                        }
                    }
                },
                {"blocked": {"$not": {"$eq": True}}},
            ]
        }
    )

    restaurants = [RestaurantModel.from_document(r).to_document() for r in cursor]
    return jsonify(restaurants)


@app.route("/api/restaurant/<rid>", methods=["GET"])
def fetch_one_restaurant(rid):
    r = collection.find_one(
        {"$and": [{"_id": ObjectId(rid)}, {"blocked": {"$not": {"$eq": True}}}]},
        {"_id": False, "blocked": False},
    )

    if not r:
        return '', 404
    return jsonify(RestaurantModel.from_document(r).to_primitive())


@app.route("/api/restaurant/<rid>", methods=["PUT"])
def update_one_restaurant(rid):
    try:
        r = RestaurantModel(request.get_json())
        r.validate()
    except DataError as e:
        return jsonify(e.to_primitive()), 400

    passcode = request.args.get("passcode")
    result = collection.update_one({"$and": [{"_id": ObjectId(rid)}, {"passcode": passcode}]}, {'$set': r.to_document()})

    if result.matched_count == 0:
        return '', 404
    else:
        return '', 204


if __name__ == "__main__":
    app.run()
