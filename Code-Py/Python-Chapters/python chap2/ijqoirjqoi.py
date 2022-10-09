word=str(input('Enter the word'))
s = word[0:1]
y = word[-1:len(word)]
for i in range (0,len(word)):
    for j in range (0, len(word)):
        s = word[(0+i):(1-j)]
        y = word[(-1-i):(1-len(word))]
print(s)
print(y)
