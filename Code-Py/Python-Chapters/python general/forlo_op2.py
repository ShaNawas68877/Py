#for loop advanced
x = int(input('Enter a number:'))
for i in range (1, x+1):
    for j in range (1, x+1):
        #print(i) #when print(i) alone is enabled, when i is 1, j loops and prints 1 five times
                    # cont... and similarly the other integers.
        print(j) #when print(j) alone is enabled, when i is 1, j loops and print j values
                   # cont... that is 1,2,3,4,5 if x is 5 and again when i is 2 prints 1,2,3,4,5,
        
