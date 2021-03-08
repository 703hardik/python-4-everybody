import json
import urllib.request, urllib.parse ,urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter location:')
print('Retrieving',url)
code=urllib.request.urlopen(url).read()
js= json.loads(code)
j1=js["comments"]

ls1=list()
for item in j1:
    ls1.append(item["count"])
print(sum(ls1))
