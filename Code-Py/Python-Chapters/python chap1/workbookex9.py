#Exercise 9 : Compound interest
deposit=float(input('Enter the amount to be deposited in the savings account:'))
#i=int(input('Enter the number of years:'))
#for i in range (0,i+1):
ci=deposit * 0.04
total = ci + deposit
second = total + total * 0.04
third = second + second * 0.04
print('The amount in the savings account after 1 year will be', format(total,'.2f'))
print('The amount in the savings account after 2 years will be', format(second,'.2f'))
print('The amount in the savings account after 3 year will be', format(third,'.2f'))
