import random
nes = []
les = []
alllist = []
deslist = []
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        z = list(z)
        print(z)
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
print(users)
for r in range(lists.n):
    out = (set(users) & set(nes[r]))
    out = list(out)
    percent = ((len(out)/len(users)) * 100)
    percent = int(percent)
    dupli = nes[:]
    print(dupli)
    for j in dupli:
        dupli = nes[:]
        for i in out:
            dupli[dupli.index(i)] = '/'+i+'/'
            for o in nes:
                les = nes.pop()
                dupli[dupli.index(i)] = '/'+i+'/'
                print(les)
                print(dupli)
        '''dupli.append(r+1)
        dupli.append(percent)
    alllist.append(dupli)
    #alllist.sort(reverse = False, key = lambda kv: kv[-1])
deslist.append(alllist)'''
