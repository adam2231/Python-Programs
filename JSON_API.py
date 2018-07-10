#Use of API & JSON - read a website page, find a University in the list and print its hidden place ID

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

seekingaddress = "IT College of Estonia"

parameters = {"sensor": "false", "address": seekingaddress}
url = serviceurl + urllib.parse.urlencode(parameters)
print('Retreiving', url)

qurl = serviceurl + url
print("Data URL:", qurl)

data = urllib.request.urlopen(qurl).read()

jsondata = json.loads(data)
id = jsondata["results"][0]["place_id"]

print("Place ID", id)
