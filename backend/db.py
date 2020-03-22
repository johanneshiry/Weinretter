from pymongo import MongoClient, GEOSPHERE, ASCENDING

client = MongoClient('mongocontainer', 27017)
db = client.weinretter
collection = db.restaurants
collection.create_index([('location', GEOSPHERE), ('blocked', ASCENDING)])
