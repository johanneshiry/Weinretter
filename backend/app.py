from flask import Flask, escape, request 
from urllib.parse import urlparse
from pymongo import MongoClient, GEOSPHERE

client = MongoClient('localhost', 27017)
db = client.weinretter
collection = db.restaurants
collection.create_index([("location", GEOSPHERE)])

app = Flask(__name__)

@app.route('/api/restaurant', methods=["POST"])
def create_restaurant():
    body = request.get_json()
    
    link = body["link"]
    # XXX URL Validation
    try:
        urlparse(link)
    except:
        return "", 400 
    name = body["name"]
    location = (body["location"]["lat"], body["location"]["lng"])
    collection.insert({"link": link, "name": name, "location": location})

    return "", 204 


