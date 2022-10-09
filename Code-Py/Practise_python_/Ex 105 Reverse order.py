x = []
i = 0
z = int(input("Enter the integers"))
while z != 0:
    x.append(z)
    z = int(input("Enter the integers"))
x.sort()
for z in x:
    while i != - len(x):
        i = i - 1
        print(x[i])
