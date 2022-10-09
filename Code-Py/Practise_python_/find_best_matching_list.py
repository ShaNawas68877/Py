import random # nested list created succesfully using Ex 104 and Ex 105
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return nes
lists(5,10)#the second argument is y
z = str(input("Enter letter (a-z)"))
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
ulist = list (z)
#print (ulist[0:10])
for r in range (9):#the range value is y
    out = (set(nes[r]) & set(ulist[0:10]))
    #if len(out) == 0:
        #print ("")#nes[r], "NOT matches with", ulist[0:10])
    #else:
        #print (nes[r], "matches with", ulist[0:10], "is", out)
        #print (nes[r], "List1 matches with", ulist[0:10], "is", out)
    if len(out) != 0:
        diff = (len(nes[r]) + 10) - len(out)# all different - all common
        tot = diff - len(out)
        percent = ( len(out) / tot ) * 100
        print("List",r, "matches %d %", percent, nes[r])
    else:
        #print("The matching percentage is 0")
        print("")
