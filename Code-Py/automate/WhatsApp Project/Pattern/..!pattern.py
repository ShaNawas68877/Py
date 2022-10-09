n = ''
m = len(n)/2
o = int(float(m))
for i in range(0,len(n)):
    if(i != (len(n)-1)):
        print(n[i] + '..',end='')
    else:
        print(n[i] + '..!')
print('enter')



##for i in range(0,len(n)):
##    if i<o:
##        print(' '*i+n[i])
##    else:
##        print(' '* ((o*2)-i)+n[i])
