# Exercise 45 : What color is that square
n = str(input('Enter the position: '))
s = n[:1]
l = n[1:]
if (s == "a" or s == "c" or s == "e" or s == "g") and (l == "1" or l == "3" or l == "5" or l == "7"):
    print("black")
elif (s == "b" or s == "d" or s == "f" or s == "h") and (l == "2" or l == "4" or l == "6" or l == "8"):
    print('black')
elif (s == "a" or s == "c" or s == "e" or s == "g") and (l == "2" or l == "4" or l == "6" or l == "8"):
    print('white')
else:
    print('white')
#elif (s == "b" or s == "d" or s == "f" or s == "h") and (l == "1" or l == "3" or l == "5" or l == "7"):
    print('black')
