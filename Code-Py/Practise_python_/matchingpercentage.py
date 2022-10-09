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
users = users[0:10]
print(users)
print("")
for r in range (1):
    out = (set(users) & set(nes[r]))
    #n = len(out)
    out = list(out)
    for i in out:
            users[users.index(i)] = '/'+i+'/'
    print(users)
percent = (4/len(users)) * 100
print(len(users))
print (percent)
