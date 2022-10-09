import random as rd
import numpy as np
nes = []
def lists(x,y):
    for i in range (x):
        z = rd.sample('abcdefghijklmnopqrstuvwxyz', y)
        z = list(z)
        lists.n = x
        nes.append(z)
    return nes
lists(5,8)
users = (input("Enter letters (a-z)"))
print("")
users = users.lower()
users = users.replace(",","")
users = users.replace(" ","")
users = list(users)
users = users[0:10]
