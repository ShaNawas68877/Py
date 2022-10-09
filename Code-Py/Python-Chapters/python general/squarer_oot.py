x=int(input('Enter the number:'))
ans = 0
while ans**2 < abs(x):
    ans = ans + 1
if ans**2 == abs(x):
    print(ans, 'is the square root of',x)
elif ans**2 != abs(x):
    print(x, 'is not the perfect square')
    
