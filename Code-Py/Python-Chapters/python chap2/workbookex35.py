# Exercise 35 : Dog Years
age = int(input('Enter the human year: '))
age1 = (age - 2) * 4
if age < 2:
    print('The equivalent dog years are', age * 10.5)
else:
    print('The equivalent dog years are', (2 * 10.5) + age1)
