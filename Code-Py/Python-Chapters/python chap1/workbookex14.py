# Exercise : Height Units

hei = float(input('Please enter your height in feet:'))
heiinch = hei * 12
centi = heiinch * 2.54
print('Your height is', format(centi,'.3f'),'centimetres')
print('Your rounded height is', round(centi), 'centimetres')
