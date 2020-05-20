import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro



#serviceurl = 'http://py4e-data.dr-chuck.net/xml?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

add=0
address = input('Enter location: ')
if len(address) < 1: exit()
url = urllib.request.urlopen(address, context=ctx)
data = url.read()
print('Retrieved', len(data), 'characters')
data.decode()
tree = ET.fromstring(data)
for i in range(0,50,1):
    a=int(tree[1][i][1].text)
    add=add+a
print("add is:",add)

#add will give you the sum
