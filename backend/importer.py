import csv
import urllib.request
import json      


with open('/Users/christophwalcher/Weinretter.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # skip the header
    for r in reader:
        if not r[4]:
            continue
        print(r)
        req = urllib.request.Request("https://weinretter.de/api/restaurants")
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        address = None
        description = None
        if not r[2] == "":
            address = r[2]
        if not r[5] == "":
            description = r[5]
        body = {"name": r[1],
                "link": r[0],
                "address": address,
                "location": {"lat": float(r[3]), "lng": float(r[4])},
                "description": description}
        print(body)
        jsondata = json.dumps(body).encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondata))
        urllib.request.urlopen(req, jsondata)

