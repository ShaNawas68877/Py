l = str(input("Enter letter (a-z)"))
l = l.replace(" ","")
l = l.replace(",","")
l = l.lower()
print(len(l))
s = l[0:10]
print ("users list =", s)
print (len(s))
print (list(s))
m = str(input("Enter letter (a-z)"))
m = m.replace(" ","")
m = m.replace(",","")
m = m.lower()
print(len(m))
n = m[0:10]
print ("users list =", n)
print (len(n))
print (list(n))
o = list(set(s) | set(n))
print (o)