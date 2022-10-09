# Exercise 58 : Next day
ye = int(input('Please enter the year:'))
mo = str(input('Please enter the month:')) #initially month was declared as int, the elif loop for mo == "02" was not read
da = int(input('Please enter the day:'))    #then changed to str it works perfectly
if da > 31:
    da = 1
    mo = mo + 1
elif mo == "02" and da == 28:
    da = 1
    mo = 2 + 1
da = da + 1
print('The next day is', da,'-',mo,'-',ye)




#if mo == 02:
 #   day = 28
#if mo == 01 or mo == 03 or mo == 05 or mo == 07 or mo == 08 or mo == 10 or mo == 0:
 #   da = da + 1
#else:
 #   day = 30

    
#https://plus.google.com/+JuliusBlake/posts/c3F6eWWYAqs
 #http://bigflix.net/watch/?movie=tt3315342
