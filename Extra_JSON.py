#Use of JSON - read and extract JSON from file, find the number of characters, and the sum of the numbers attached to strings

import urllib.request, urllib.parse, urllib.error
import json

Jurl = input('Enter location: ')
print ('Retrieved:', Jurl)
uh = urllib.request.urlopen(Jurl)
data = uh.read().decode('utf-8')
print ('Retrieved:', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

x = 0
for items in js["comments"]:
    x = x + int(items["count"])
print("Sum:", x)
