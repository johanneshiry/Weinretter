from flask import Flask, escape, request, status
from urllib2 import urlopen
from pymongo import MongoClient, GEO2D

client = MongoClient('localhost', 27017)


app = Flask(__name__)

@app.route('/api', methods=["POST"])
def hello():
    body = request.json
    
    link = body["link"]
    # XXX URL Validation
    try:
        urlopen(link)
    except ValueError:
        return "", HTTP_400_BAD_REQUEST
    name = body["name"]
    location = (body["location"]["lat"], body["location"]["lng"])


    return "", HTTP_204_NO_CONTENT

