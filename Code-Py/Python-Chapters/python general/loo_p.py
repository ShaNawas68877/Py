# Exercise 61.1 : Average   # average of 1 to num numbers
num = int(input('Enter the number:'))
x = 1
for num in range (0,num):
    num = num + 1
    x = num + x
y = (x - 1) / num
print(y)
