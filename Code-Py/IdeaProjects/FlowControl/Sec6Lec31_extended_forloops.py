number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ['not pinin', 'no more','a stiff', 'beret of life']:
    print('This parrot is '+state)

for i in range(0,100,5):
    print('i is {}'.format(i))

for i in range(0,13):
    for j in range(0,13):
        print('{1} times {2} is {0}'.format(i * j, i, j), end='\t')
    print('')
    #print('"""""""""""""""""""""""""""')