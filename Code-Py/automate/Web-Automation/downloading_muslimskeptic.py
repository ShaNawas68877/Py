import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#for div in BeautifulSoup(urlopen(
req = requests.get("https://muslimskeptic.com/2017/06/09/1141/", headers={'User-Agent': 'Mozilla/5.0'})
page = BeautifulSoup(req.content, "html.parser")
final = page.encode('utf-8')
vvv = page.findAll('div', {'class':'entry-content-single'})
for p in vvv:
    print(p.text)
