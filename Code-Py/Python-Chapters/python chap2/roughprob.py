# Exercise 58 : Next day
ye = int(input('Please enter the year:'))
mo = str(input('Please enter the month:'))
da = int(input('Please enter the day:'))
#if da > 31:
 #   da = 1
  #  mo = mo + 1
if mo == "02" and da == 28:
    da = 1
    mo = 2 + 1
da = da + 1
print('The next day is', da,'-',mo,'-',ye)
