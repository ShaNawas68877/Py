#Exercise 15 : Distance units

num = float(input('Please enter the distance in feet: '))
inch = num * 12
yard = num * 0.333333
miles = num * 0.000189394
print('The entered distance is', inch,'inches')
print('The entered distance is', format(yard,'.3f'),'yards')
print('The entered distance is', miles,'miles')
