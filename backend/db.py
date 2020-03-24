from pymongo import MongoClient, GEOSPHERE, ASCENDING

client = MongoClient('mongocontainer', 27017)
db = client.weinretter
collection = db.restaurants
collection.create_index([("location", GEOSPHERE), ("blocked", ASCENDING)])
passcode_collection = db.passcodes
passcode_collection.create_index(
    [("restaurant_id", ASCENDING), ("passcode", ASCENDING)]
)
