#Exercise 10 : Arithmetic

from math import log10  # To use log function in this case
a=float(input('Enter the first number:'))
b=float(input('Enter the second number:'))
su=a+b
dif=a-b
pro=a*b
quo=a/b
remainder=a%b
#log=(log2)/(logb) #log cannot be found using log as an operator
exp=a**b
print('The sum of a and b is', su)
print('The difference of a and b is', dif)
print('The product of a and b is', pro)
print('The quotient of a and b is', quo)
print('The remainer of a and b is', remainder)
print('The base 10 log of a is', log10(a))  #from import should always be used
print('The exponential of a and b is', exp)
