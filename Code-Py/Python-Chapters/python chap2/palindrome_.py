#Exercise 72 : Is string a palindrom?
word = str(input('Enter the word'))
s = word[:1]
n = word[1:]
for i in range (0,len(word)):
    s = word[1:]
    n = word[:1]
    i = i + 1
    if s == n:
        print('Yes')
print(s)
print(n)
