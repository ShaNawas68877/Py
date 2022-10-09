import random # nested list created succesfully using Ex 104 and Ex 105
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        #z = [ random.choice('abcdefghijklmnopqrstuvwxys') for _ in range (y) ]
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    print (nes)
lists(5,5)
print (nes[5])
