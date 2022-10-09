import random
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return nes
lists(1,8)
z = str(input("Enter letters (a-z)"))
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
users = list (z)
print("")
print(users)
'''out = (set(nes) & set(users[0:10]))
out = list(out)
print(out)'''



#out = (set(nes) & set(users[0:10]))
#out = list(out)
print(nes[0])
out = ['/{}/'.format(l) if l in nes else l for l in users]
out = list(out)
print(out)
'''for i in out:
    users[users.index(i)] = '/'+i+'/'
print(users)







print(nes[0])
out = (set(users).intersection(nes[0]))
out = list(out)
print(out)
for i in out:
    users[users.index(i)] = '/'+i+'/'
print(users)
'''
