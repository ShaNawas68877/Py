#Extending For Loops

for state in ['not pinning', 'no more', 'a stiff', 'bereft of life']:
    print('This parrot is ' + state)

for i in range (0,100,5):
    print("i is {}".format(i))

for i in range(1,13):
    for j in range (1,13):
        print("{1} times {0} is {2}".format(i,j, i*j), end='\t')
    #print("======================")
