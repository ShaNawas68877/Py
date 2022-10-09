# Exercise 71 : Square Root
x = float(input('Enter the number to find its square root'))
guess = x / 2
while (x  != guess * guess):
    guess = (guess + ( x / guess)) / 2
if guess != guess * guess:
    print('next step?')
print(guess)
