import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#for div in BeautifulSoup(urlopen(
req = requests.get("https://www.offensive-security.com/metasploit-unleashed/", headers={'User-Agent': 'Mozilla/5.0'})
page = BeautifulSoup(req.content, "html.parser")
final = page.encode('utf-8')
vvv = page.findAll('a',href=True)
for p in vvv:
    print(p.text.href)
