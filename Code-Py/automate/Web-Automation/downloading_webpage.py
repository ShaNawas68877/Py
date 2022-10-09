import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
n = res.status_code# == requests.codes.ok
print(n)
print(res.text[:2500])
