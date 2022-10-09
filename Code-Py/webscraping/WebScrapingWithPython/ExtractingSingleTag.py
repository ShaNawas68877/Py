#pg no 27
#from urllib.request import urlopenf
import urllib.request
import html.parser
import html5lib
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup
soup = bs4.BeautifulSoup(html, 'lxml')
html1 = urlopen('http://www.pythonscraping.com/exercises/exercise1.html')
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
