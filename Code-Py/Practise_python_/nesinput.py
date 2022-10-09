import random # nested list created succesfully using Ex 104 and Ex 105
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        #z = [ random.choice('abcdefghijklmnopqrstuvwxys') for _ in range (y) ]
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return (nes)
lists(5,5)
#print (nes[3])
z = str(input("Enter the alphabets"))
'''while len(z) > 10:
    z = str(input("Enter the alphabets"))
print (len(z))
x = z[0:10]
#print (len(x))'''
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
x = list (z)
print (x[0:10])
#print (nes[0])
for r in range (5):
    out = (set(nes[r]) & set(x[0:10]))
    if len(out) == 0:
        out = "nothing matches"
    print (nes[r], "matches with", x[0:10], "is", out)
#print (len(out))
