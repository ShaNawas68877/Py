#Ex 104 : Sorted order
#z = list # cannot do further , cannot make it enter 0 as 0 is int
'''while z != 0:
    z = list(input("Enter the integers ( 0 to quit )"))
print (z)
print (z.sort())'''

z = int(input("Enter the integers ( 0 or blank to quit )"))
x = []
try:
    while z != 0:
        x.append(z)
        z = int(input("Enter the integers ( 0 or blank to quit )"))
    print (z)
    x.sort()
    for z in x:
        print (z)
except ValueError:
    x.sort()
    for z in x:
        print(z)
    

