#! python3
# opening_first5_searches.py - opens several Google search results.
import requests, sys, webbrowser, bs4
print('Googling.....')
n = input('Enter the search term')
res = requests.get('https://www.google.co.in/search?q='+n)#''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range (numOpen):
    webbrowser.open('https://google.com'+linkElems[i].get('href'))
