#Use of BeautifulSoup to parse HTML data and find specific names in a hidden HTML data webpage

import urllib.request
from bs4 import BeautifulSoup
import ssl

url =  'http://py4e-data.dr-chuck.net/known_by_Rumaysa.html'
count = 7 + 1
position = 18 - 1
urllist = []
taglist = []

connections = 0
while connections < 7 :
    taglist = []
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for i in range(count):
        for tag in tags:
            taglist.append(tag)

    url = taglist[position].get('href', None)
    urllist.append(url)

    connections = connections + 1
print ("Retreiving:", url)
