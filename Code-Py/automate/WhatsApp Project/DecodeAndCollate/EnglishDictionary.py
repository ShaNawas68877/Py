##def loadDictionary():
##
##    dictionaryFile = open('EnglishDictionary.txt')
##    englishWords = {}
##    for word in dictionaryFile.read().split('\n'):
##        englishWords[word] = None
##        dictionaryFile.close()
##        return englishWords
##
##ENGLISH_WORDS = loadDictionary()

with open('EnglishDictionary.txt', 'r') as ding:
    engd = ding.read()
    engdlist = engd.split()

with open('stringUpperTest.txt', 'r') as reader:
    gandhi = reader.read()
    gandhilist = gandhi.split()
    
##    print(gandhilist)

with open('noteng.txt', 'w') as writer:
    b = []
    for a in gandhilist:
        if a not in engdlist:
            b.append(a)

    c = ' '
    d = c.join(b)
    writer.write(d)
            


##for b in ENGLISH_WORDS:
##    print(type(b))
##    print(b)
##
##print(ENGLISH_WORDS)
##        
##    i=0
##    print(type(gandhi))
##    for a in gandhi:
##        print(a[i])
##        i += 1
        
##        for b in ENGLISH_WORDS:
##            if b not in gandhi:
##                print(a)
##        
##    gandhi1 = gandhi.replace('nationalist','')
##with open('gandhi2.txt', 'w') as writer:
##    writer.write(gandhi1)
