n = 'I am here'
p = n.split(' ')
##print(len(p[0]))
##q = list(p)
##print(p[0])
##print(p[0][1])

##print(len(p))
##print(p)
for j in range(0, len(p)):
    for i in range(0, len(p[j])):
        if(i != (len(p[j])-1)):
           print(p[j][i] + '..',end='')
        else:
           print(p[j][i] + '..!')

        
##        if(i != (len(p)-1)):
##            print(p[j,i] + '..',end='')
##        else:
##            print(p[j,i] + '..!')

    
##    print(p[i]) I thought "LOVE" is love but just realised its just U
##    print(n[i])
##m = len(n)/2
##o = int(float(m))
##for i in range(0,len(n)):
##    if(i != (len(n)-1)):
##        print(n[i] + '..',end='')
##    else:
##        print(n[i] + '..!')
##print('enter')



##for i in range(0,len(n)):
##    if i<o:
##        print(' '*i+n[i])
##    else:
##        print(' '* ((o*2)-i)+n[i])
