#Exercise 16 : Area and volume

from tkinter import * # python -m tkinter in cmd prompt
radius = float(input('Enter the radius in centimeters: '))
area = (22/7) * (radius * radius)
volume = (4/3) * (22/7) * (radius * radius * radius)
print('The area of the circle is', area, ' square centimetres')
print('The volume of the circle is', volume,'cubic centimetres')
