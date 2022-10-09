# Exercise 79 : Maximum Integer
import random
x = random.randint(0,100)
j = 0
for i in range (0,99):
    y = random.randint(0,99)
    print(y)
    if y > x:
        print(y,"<--update")
        x = y
        j = j + 1
print("The maximum value found is ",x)
print("The maximum value was updated %d times" %j)
