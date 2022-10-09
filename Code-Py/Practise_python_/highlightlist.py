import random
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return nes
lists(5,8)
z = str(input("Enter letters (a-z)"))
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
users = list (z)
print("")
for r in range (5):
    out = (set(nes[r]) & set(users[0:10]))
    out = list(out)
    j = 0
    while j == 8:
        if out[j] == nes[r]:
            print("/"+nes[r]+"/")
    if len(out) != 0:
        diff = (len(nes[r]) + 10) - len(out)
        tot = diff - len(out)
        percent = ( len(out) / tot ) * 100
        print('List{}'.format(r+1),'matches %.2f' % (percent)+"%",":", nes[r])
    else:
        print()    # print("List{}".format(r+1),"matches 0\t\t",":", nes[r])
