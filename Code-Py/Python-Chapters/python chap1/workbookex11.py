#Exercise 11 : Fuel Efficiency
# 1 gallon = 3.79541 litres    #1 litre = 0.26417 gallons
# 1 mile = 1.60934 KM          #1KM = 0.62137 miles
fu=float(input('Please enter the fuel efficiency in MPG:'))
#miles / gallon = 0.26417 / 62.137  = 0.00425
conv =  fu / 0.00425
print('The fuel efficiency in canadian units is', format(conv,'.2f')) # format is to truncate decimal after two places
