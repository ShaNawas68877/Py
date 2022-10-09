import random
nes = []
def lists(x,y):
    for i in range (x):
        #z = [ random.choice('abcdefghijklmnopqrstuvwxys') for _ in range (y) ]
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        ne = nes.append(z)
    print (ne)
    return x
lists(5,5)
