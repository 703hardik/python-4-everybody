import re
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter URL :')
html= urllib.request.urlopen(url).read()
soup= BeautifulSoup(html,'html.parser')
links= soup('a')
exp=re.compile(r'href=\"(.+)\"')

r=list()
for link in links:

    r.append(exp.split(str(link)))
print(r)
exp2=re.compile(r'>(.+)<\/a>')
print(exp2.findall(r[0][2]))
#findall', 'finditer', 'flags', 'fullmatch',
#'groupindex', 'groups', 'match', 'pattern',
#'scanner', 'search', 'split', 'sub', 'subn'

#count=int(input('Enter count :'))
#pos=int(input('Enter position :'))
# for x in range(count):
#     html= urllib.request.urlopen(links[pos-1]).read()
#     print("Retrieving:",html)
#     soup=BeautifulSoup(html,'html.parser')
