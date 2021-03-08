import re
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#taking values from the user
url=input("Enter URL: ")
count=int(input("Enter count: "))
position=int(input("Enter position: "))
pos=position-1
exp=re.compile(r'href=\"(.+)\"')
exp2=re.compile(r'>(.+)<\/a>')
r=list()
name=str()
for x in range(count):
    html=urllib.request.urlopen(url).read()
    print('Retrieving:',url)
    soup=BeautifulSoup(html,'html.parser')
    links=soup('a')
    for link in links:
        r.append(exp.split(str(link)))

    url=r[pos][1]
    name=exp2.findall(r[pos][-1])
    r.clear()
print(name)
