import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse , urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a valid url')
html= urllib.request.urlopen(url).read()

soup= BeautifulSoup(html,'html.parser')

exp= re.compile('[0-9]+')

x=list()

tags=soup('span')

z=list()
for tag in tags:
    x.append(exp.findall(str(tag)))
for y in x:
    for a in y:
        z.append(int(a))

print(sum(z))
