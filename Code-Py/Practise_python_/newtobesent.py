import random
nes = []
#i = 0
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        lists.n = x
        nes.append(z)
    return nes
lists(5,8)
#print(lists.n)
z = (input("Enter letters (a-z)"))
z = z.lower()
t = []
z = z.replace(",","")
z = z.replace(" ","")
users = list (z)
users = users[0:10]
print("")
alllist = []
n = list
descending = []
for r in range (lists.n):
    out = (set(users) & set(nes[r]))
    out = list(out)
    #print(out)
    #print(len(out))
    percent = ((len(out)/len(users)) * 100)
    dupli = users[:]
    for j in dupli:
        dupli = users[:]
        for i in out:
            dupli[dupli.index(i)] = '/'+i+'/'
    #print('list{}'.format(r+1),"matches %.0f" % (percent)+"%",':',dupli)
    alllist.append(percent)
    #percent = ((len(out)/len(users)) * 100)
    dupli.append(percent)
    print(dupli)
    descending.append(dupli)
    descending.sort()
    alllist.append (dupli)
    sorted(dupli.percent(), key = lambda kv: kv[1])
    print(dupli)
    
    #print('list{}'.format(r+1),"matches %.0f" % (percent)+"%",':',alllist)
    #print(dupli)

'''
for k in range (lists.n):   
    print('list{}'.format(r+1),"matches %.0f" % (percent)+"%",':',descending[k])'''
'''
    #print(dupli)
#print(alllist)
#alllist.sort()
#print(alllist)
    for k in descending:
        print('list{}'.format(r+1),"matches %.0f" % (percent)+"%",':',descending)
#print('list{}'.format(r+1),"matches %.0f" % (percent)+"%",':',descending)'''
'''
    if len(out) != 0:
        diff = (len(nes[r]) + 10) - len(out)
        tot = diff - len(out)
        percent = ( len(out) / tot ) * 100
        print('List{}'.format(r+1),'matches %.2f' % (percent),":", nes[r])
    else:
        print("List{}".format(r+1),"matches 0\t\t",":", nes[r])'''
