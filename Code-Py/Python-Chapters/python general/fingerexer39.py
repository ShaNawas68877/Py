x = int(input('Enter the number:'))
root=0
power=2
while root**power < abs(x):
    root = root + 1
if root**power == abs(x):
    print(root)
    print(power)
else:
    power = power + 1
    #print(power)
    root = 0
    while root**power < abs(x):
        root = root + 1 
if root**power == abs(x):
    print(root)
    print(power)
    
    #if root**power < abs(x):
     #   power = power + 1
    
    
#while power > 6:
 #   break
#print(root)
#print(power)

        
