# Exercise 56 : Cell Phone Bill

minu = int(input('Please enter the number of minutes:'))
mess = int(input('Please enter the number of text messages:'))
print("The base charge is $15.00")
if minu > 50:
    ach = ( minu - 50 ) * 0.25  #ach = additional charge
    print("The additional minutes charge is $"+format(ach,'.2f'))
    #print("The additional minutes charge is $"+ach)  the concatenate to $ does not work if format specifier is not used
    #print("The additional minutes charge is $"+float(ach)) even ach is made float still it does not work
elif minu <= 50:
    ach = 0
if mess > 50:
    achm = ( mess - 50 ) * 0.15
    print("The additional messages charge is $"+format(achm,'.2f'))
elif mess <= 50:
    achm = 0
print('The 911 fee is $0.44')
tot = 15 + ach + achm + 0.44
gtot = tot + ( tot * 0.05)
print("The Grand total bill is $"+format(gtot,'.2f'))
