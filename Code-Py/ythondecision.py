import random
a = "Data Science"
b =  "Infosec"
c = "Day Shift"
d = "Night Shift"
e = 0
f = 0
g = 0
h = 0
i = 0
def decisionmaker():
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    while e < 101:
        rint = random.randint(1,4)
        if rint == 1:
            f +=1
        elif rint == 2:
            g += 1
        elif rint == 3:
            h+=1
        else:
            i+=1
        e += 1
    print("Percentage for {} is {}%".format(a,f))
    print("Percentage for {} is {}%".format(b,g))
    print("Percentage for {} is {}%".format(c,h))    
    print("Percentage for {} is {}%".format(d,i))

    if (f > g) and (h > i):
        print("Data Sciece and Day Shift")
    else:
        print("Incorrect result")
        decisionmaker()

decisionmaker()    
##
##while True:
##    rint = random.randint(0,2)
##    print(rint)
