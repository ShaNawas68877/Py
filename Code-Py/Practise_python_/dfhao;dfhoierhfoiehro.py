import random
i = 0
j = 0
for x in range (0,99):
   # i = 0
    #j = 0
    y = random.randint(0,99)
    if y > 50 and i <= 2:
        print('H')
        i = i + 1
        if i > 2 :
            print(i)#, "got it")
            break
        j = 0
    elif y < 50 and j <= 2:
        print('T')
        j = j + 1
        i = 0
        if j > 2:
            print('got it')#, "another got it")
            break
        
