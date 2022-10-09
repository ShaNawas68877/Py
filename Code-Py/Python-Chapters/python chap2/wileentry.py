from math import *
perimeter = 0
first_x = float(input('Enter the x part'))
first_y = float(input('Enter the y part'))
prev_x = first_x
prev_y = first_y
line = input("enter the x part(blank to quit")
while line != "":
    x = float(line)
    y = float(input("Enter the y part of the co ordiantes:"))

    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

    prev_x = x
    prev_y = y

    line = input("Enter the x part (blank to quit)")

dist = sqrt((first_x - x) ** 2 + (first_y) ** 2 )
perimeter = perimeter + dist
print("the perimeter is", perimeter)
