import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



address = input('Enter location: ')
if len(address) < 1: exit()
url = urllib.request.urlopen(address, context=ctx)
data = url.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data.decode())
a=0
li=info["comments"]
for item in li:
    a=a+item["count"]
print("count is:",a)


#Count is the answer
