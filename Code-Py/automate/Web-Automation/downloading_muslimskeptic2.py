import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#for div in BeautifulSoup(urlopen(
req = requests.get("https://muslimskeptic.com/2016/07/25/silly-atheistic-arguments/", headers={'User-Agent': 'Mozilla/5.0'})
page = BeautifulSoup(req.content, "html.parser")
final = page.encode('utf-8')
title = page.find('h1', {'class':'entry-title'})
print(title.text)
content = page.findAll('div', {'class':'entry-content-single'})
for p in content:
    print(p.text)
