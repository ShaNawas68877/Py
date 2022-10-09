#Exercise 7 : Sum of the First n Positive integers
n=int(input('Enter the Positive integer:'))
s = n * (n + 1)#if n + 1 is not bracketed then the result will be wrong
s/=2
print('The sum of the first', int(n), 'positive integers is', int(s))
