import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# inputing the url
url= input('Enter Location:')
print("retrieving",url)
xml= urllib.request.urlopen(url).read()

tree=ET.fromstring(xml) #parsing of xml

lst=tree.findall('comments/comment') #giving path in treee form

lis=list()
for lt in lst:
    lis.append(int(lt.find('count').text))
print('sum',sum(lis))
