# Exercise 37 : Name that shape
s = int(input('Enter the number of sides of the shape: '))
if s == 3:
    print('This is a triange')
elif s == 4:
    print('This is a square')
elif s == 5:
    print('This is a pentagon')
elif s == 6:
    print('This is a hexagon')
elif s == 7:
    print('This is a heptagon')
elif s == 8:
    print('This is a octagon')
elif s == 9:
    print('This is a nonagon')
elif s == 10:
    print('This is a decagon')
else:
    print('Error : the number entered is out of range')
