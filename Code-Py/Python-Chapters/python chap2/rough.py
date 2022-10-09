let = str(input('Please enter your letter Grade: '))
s = let[:1]
sy = let[1:]
t = "Your Grade point is"
if let == "A" or let == "B" or let == "C" or let == "D":
    b = '.0'
if let == "A+" or let == 'A':
    a = '4'
    b = '.0'
elif let == "A-":
    a = '3'
if s == "C" and (sy == "+" or sy == ''):
    a = '2'
elif (s == 'C' and sy == '-') or s == 'D':
    a = '1'
if sy == '+':
    b = '.3'
if sy == '-':
    b = '.7'
print(a+b)
