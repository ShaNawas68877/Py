#SEARCH THE KEYWORDS IN ANY WEBSITE: 1. TAKE KEYWORDS FROM PYTHON_MAN TEXT FILE  2. APPEND IT TO THE BASE URL 3. OPEN IT IN THE BROWSER

import webbrowser

baseUrl = "https://amazon.in/s?k="

f = open('python_man.txt','r')
keywordFile = f.read()
keyword = keywordFile.splitlines()
keywordLen = len(keyword)
for i in range(keywordLen):
    url = baseUrl+keyword[i]
    webbrowser.open(url,new=2)
