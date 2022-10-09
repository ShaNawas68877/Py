#Exercise 6 : Tax and Tip
cost=float(input('Enter the Cost of the meal in dollars:'))
tax = cost * 0.05
tip = cost * 0.18
print('The tax amount for the meal you had is $'+format(tax,'.2f'))#format specifier is used to round the dollar amount to two digits
print('The tip amount for the meal you had is $'+format(tip,'.2f'))
total = cost + tax + tip
print('The grand total amount is $'+format(total,'.2f'))
