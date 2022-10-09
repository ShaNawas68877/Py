import random
import string
randAlp = string.ascii_lowercase
x = 3
y = 5
list1 = []
list2 = []
for j in range(0,x):
    for i in range(0,y):
        list1.append(random.choice(randAlp))
    list2.append(list1)
print(list2)
