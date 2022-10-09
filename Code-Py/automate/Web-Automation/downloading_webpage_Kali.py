##import requests
##res = requests.get('https://www.offensive-security.com/metasploit-unleashed/').
##print(type(res))
##n = res.status_code# == requests.codes.ok
##print(n)
##print(res.text[:2500])

import requests
from lxml.html import fromstring
r = requests.get('http://www.imdb.com/title/tt0108778/')
tree = fromstring(r.content)
for i in tree.findtext('.//title'):
    print(i)

