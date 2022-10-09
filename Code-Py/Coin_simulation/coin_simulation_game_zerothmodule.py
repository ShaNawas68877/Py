# Exercise 80 : Coin simulation # one of the toughest program
import random
i = 0
j = 0
k = 0
for x in range (0,99):
    y = random.randint(0,99)
    k = k + 1
    if (y % 2 == 0) and i <= 2:
        last = 'H'
        print(last, end = " ")
        i = i + 1
        if i > 2 :
            #print(i)
            break
        j = 0
    elif (y % 2 == 1) and j <= 2:
        last = 'T'
        print(last, end = " ")
        j = j + 1
        i = 0
        if j > 2:
            #print('got it')
            break
print("(%d continuous flips)" % k)
if last == 'H':
    print('you got a point')
elif last == 'T':
    print('You lost a point')
