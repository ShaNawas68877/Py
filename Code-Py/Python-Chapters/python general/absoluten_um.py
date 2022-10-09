x = int(input('Enter the number:'))
print(abs(x))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x,'is not a perfect cube')
elif x < 0:
        ans = -ans
        print('cube root of', x,'is', ans)
elif x > 0:
    print('cube root of', x,'is', ans)
