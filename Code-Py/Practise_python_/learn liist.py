import random
l = str(input("Enter letter (a-z)"))
l = l.replace(" ","")
l = l.replace(",","")
l = l.lower()
print(len(l))
s = l[0:10]
print ("users list =", s)
print (len(s))
print (list(s))
z = [random.choice('abcdefghijklmnopqrstuvwxys') for _ in range (10) ]
print (z)
n = list(set(s) & set(z))
print (n)
