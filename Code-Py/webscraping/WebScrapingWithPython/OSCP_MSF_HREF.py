import useragent
import urllib.request
from bs4 import BeautifulSoup
import bs4
headers = {'User-Agent': 'Mozilla/5.0'}
#from html.parser import HTMLParser
#html.encode('latin-1').decode('gbk').encode('utf-8')
url = "https://www.offensive-security.com/metasploit-unleashed/"
htmlfile = urllib.request.urlopen(url)
##for links in soup.findAll('a'):
##    print(links.get('href'))
soup = BeautifulSoup('lxml',htmlfile)
for span in soup.find('a'):
    print(links.get('href').text)


