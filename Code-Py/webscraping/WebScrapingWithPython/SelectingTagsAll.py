from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.offensive-security.com/metasploit-unleashed/')
bsObj = BeautifulSoup(html.read())
nameList = bsObj.findAll('span')
for name in nameList:
    print(name.get_text())
