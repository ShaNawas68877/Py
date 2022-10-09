#Exercise 104 : Sorted Order
data  = []
a = int(input("Enter the integers(0 to quit)"))
while a != 0:
    data.append(a)
    a = int(input("Enter the integers(0 to quit)"))
for a in data:
    print(data.sort())
    
