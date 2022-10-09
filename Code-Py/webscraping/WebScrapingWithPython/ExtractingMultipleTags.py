from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read())
nameList = bsObj.findAll('span',{'class':'green'})
for name in nameList:
    #print(name)          #(prints with tags)
#for name in nameList:
    print(name.get_text())#get_text attribute prints only the content without tags
