# Exercise 47 : Birth Date to Astrological Sign          #The program should work for any year
year = int(input('Enter the year to get your animal: ')) # so im getting the input and im adding 12, coz the animal rotates for every 12 months
y = year + 12                                            # next im getting the remainder, if the remainder is 8 then obviously it is multiple of 2012 + 12x   
s = y % 12
if year == 2000 or s == 8:
     t = "Dragon"
elif year == 2001 or s == 9 :
    t = "Snake"
elif year == 2002 or s == 10 :
    t = "Horse"
elif year == 2003 or s == 11 :
    t = "Sheep"
elif year == 2004 or s == 0 :
    t = "Monkey"
elif year == 2005 or s == 1 :
    t = "Rooster"
elif year == 2006 or s == 2 :
    t = "Dog"
elif year == 2007 or s == 3 :
    t = "Pig"
elif year == 2008 or s == 4 :
    t = "Rat"
elif year == 2009 or s == 5 :
    t = "Ox"
elif year == 2010 or s == 6 :
    t = "Tiger"
elif year == 2011 or s == 7 :
    t = "Hare"
print(t)
