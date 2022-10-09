import random # nested list created succesfully using Ex 104 and Ex 105
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return nes
lists(5,8)#the second argument is y
z = str(input("Enter the alphabets"))
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
ulist = list (z)
print("")
for r in range (5):#the range value is x
    out = (set(nes[r]) & set(ulist[0:10]))
    #if len(out) == 0:
       # print (nes[r], "NOT matches with", ulist[0:10])
   # else:
    #    print (nes[r], "matches with", ulist[0:10], "is", out)
    if len(out) != 0:
        diff = (len(nes[r]) + 10) - len(out)# all different - all common
        tot = diff - len(out)
        percent = ( len(out) / tot ) * 100
        print('List{}'.format(r+1),'matches %f' % (percent),":", nes[r])
    else:
        print("List{}".format(r+1),"matches 0",":", nes[r])
