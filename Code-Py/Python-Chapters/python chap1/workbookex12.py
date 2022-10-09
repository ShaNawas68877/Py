#Exercise 12 : Distance between two points on Earth

#import math    #if we use this(import math) then wherever we use this function
                # .... should use math.acos(x)
from math import *   # if we use this (from math import *) we just can use cos(x)
                     # no need to use math.cos(x) any more, this is efficient
latt1=float(input('Please enter the first point\'s Latitude:'))#13.0827
latt1r = radians(latt1) # very crucial, i missed, user gives input in degrees this function radians(x) is used to convert that into radians
long1=float(input('Please enter the first point\'s Longitude:'))#80.2707
long1r = radians(long1)  # very crucial, i missed, user gives input in degrees this function radians(x) is used to convert that into radians
latt2=float(input('Please enter the second point\'s Latitude:'))#11.0168
latt2r= radians(latt2)   # very crucial, i missed, user gives input in degrees this function radians(x) is used to convert that into radians
long2=float(input('Please enter the second point\'s Longitude:'))#76.9558
long2r= radians(long2)   # very crucial, i missed, user gives input in degrees this function radians(x) is used to convert that into radians
#distance = 6371.01 * math.acos(math.sin(latt1) * math.sin(latt2) + math.cos(latt1) * math.cos(latt2) * math.cos(long1 - long2))
distance = acos((sin(latt1r) * sin(latt2r)) + (cos(latt1r) * cos(latt2r) * cos(long1r - long2r)))
actual = 6371.01 * distance
print('The distance between two points on the earth is', actual)
# 1 rad = 57.2958 degrees
