import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#for div in BeautifulSoup(urlopen(
req = requests.get("https://peacenikkahmatrimony.com", headers={'User-Agent': 'Mozilla/5.0'})
page = BeautifulSoup(req.content, "html.parser")
final = page.encode('utf-8')
#title = page.find('h1', {'class':'entry-title'})
#print(title.text)
content = page.findAll('div', {'class':'prof_data'})
for p in content:
    print(p.text)
