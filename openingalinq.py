import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url="https://www.py4e.com/tools/python-data/?PHPSESSID=e141e6735d61876128a1400b385b39f0"
html= urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
text=soup('script')
