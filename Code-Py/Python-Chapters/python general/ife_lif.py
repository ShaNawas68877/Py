x=int(input('enter the number:'))
if x%11==0 and x%12 ==0:
      print(x,'is divisible by both 11 and 12')
elif x%11==0:
      print(x,'is divisible by only 11')
elif x%12==0:
      print(x,'is divisible by 12')
else:
    print(x,'is not divisible by 11 or 12')

