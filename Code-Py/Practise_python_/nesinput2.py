import random # nested list created succesfully using Ex 104 and Ex 105
nes = []
i = 0
def lists(x,y):
    for i in range (x):
        #z = [ random.choice('abcdefghijklmnopqrstuvwxys') for _ in range (y) ]
        z =  random.sample('abcdefghijklmnopqrstuvwxys', y)
        nes.append(z)
    return nes
    return y #to declare variable out of this function
lists(5,5)
#print (nes[3])
z = str(input("Enter the alphabets"))
'''while len(z) > 10:
    z = str(input("Enter the alphabets"))
print (len(z))
x = z[0:10]
#print (len(x))'''
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
ulist = list (z)
print (ulist[0:10])
#print (nes[0])
for r in range (y):
    out = (set(nes[r]) & set(ulist[0:10]))
    if len(out) == 0:
        out = "nothing matches"
    print (nes[r], "matches with", ulist[0:10], "is", out)
    if len(out) != 0:
        diff = (len(nes[r]) + 10) - len(out)# all different - all common
        tot = diff - len(out)
        percent = ( len(out) / tot ) * 100     
    else:
        percent = "0"
        '''if len(out) == 1:
                    print ("The matching percentage is", 
                print ("The matching percentage is''' 
    print ("The matching percentage is", percent) 
#print (len(out))

'''
    diff = 10 - 5
    diff2 = diff - out
    percent = diff2 % 10
    percent2 = percent * 100
'''
