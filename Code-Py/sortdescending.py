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
    try:
        out = (set(users) & set(nes[r]))
        out = list(out)
    except:
        IndexError
    percent = ((len(out)/len(users)) * 100)
    percent = int(percent)
#print(nes)
    for m in nes:
        dupli = nes[:]
        print(nes)
        for j in dupli:
            dupli = nes[:]
            print(nes)
            for k in range(5):
                try:
                    les = nes.pop()
                    print(les)
                except:
                    IndexError
            '''for i in out:
                dupli[dupli.index(i)] = '/'+i+'/'
                print(dupli)'''
