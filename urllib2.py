import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

c=int(input('Enter count - '))
pos=int(input('Enter position -'))
l1=[]
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
	l=link.get('href')
	l1.append(l)
print("link:",l1[pos-1])
for i in range(0,c-1,1):
	url=l1[pos-1]
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	l1=[]
	for link in soup.find_all('a'):
		l=link.get('href')
		l1.append(l)
	print("link:",l1[pos-1])
  
  #the last line will give you the answer
