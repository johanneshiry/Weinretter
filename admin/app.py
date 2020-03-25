from flask import Flask

import flask_admin as admin
from flask_basicauth import BasicAuth
from flask_mongoengine import MongoEngine
from flask_admin.contrib.mongoengine import ModelView
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("PASSWORD")
app.config['BASIC_AUTH_FORCE'] = True
BasicAuth(app)

app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {'DB': 'weinretter'}

# Create models
db = MongoEngine()
db.init_app(app)


class Address(db.EmbeddedDocument):
    housenumber = db.StringField()
    street = db.StringField()
    plz = db.StringField()
    city = db.StringField()


class Restaurants(db.Document):
    name = db.StringField()
    link = db.StringField()
    description = db.StringField()
    passcode = db.StringField()
    telephone = db.StringField()
    tags = db.ListField(db.StringField())
    location = db.GeoPointField()
    address = db.EmbeddedDocumentField(Address)
    blocked = db.BooleanField()


class RestaurantView(ModelView):
    column_searchable_list=('name', 'link')
    form_subdocuments = {
        'address': {
            'form_columns': ('housenumber', 'street', 'plz', 'city',)
        }
    }


admin = admin.Admin(app, 'Weinretter')
admin.add_view(RestaurantView(Restaurants))

if __name__ == '__main__':
    app.run(port=5002)
