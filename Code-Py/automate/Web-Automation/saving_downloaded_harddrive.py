import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
'''print(type(res))
n = res.status_code# == requests.codes.ok
print(n)
print(res.text[:2500])'''
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
