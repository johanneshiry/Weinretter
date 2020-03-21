## Backend

Installation via: `pip3 install -r requirements.js`
Development run: `FLASK_APP=app.py flask run`


### Endpoints:

Create restaurant:
`curl -d '{"name": "La Piazza", "link": "https://pizza.de", "location": {"lat": 48.04, "lng": 9}}' -H "Content-Type: application/json" http://localhost:5000/api/restaurant`

Query restaurants by coords:
`curl "http://localhost:5000/api/restaurant?left_lng=9&right_lng=10&bottom_lat=30&top_lat=50"`
