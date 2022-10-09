n = 'How are you'
m = len(n)/2
o = int(float(m))
print(o)

print(len(n))
print(len(n)/2)
##for(i=0,i<
##print(n[0])
##print(len(n))
##for i,j in zip(range(0,5),range(0,len(n))):
##    print(' '*i + n[j])


for i in range(0,len(n)):
    if i<o:
        print(' '*i+n[i])
    else:
        print(' '* ((o*2)-i)+n[i])





##for i in range(0,len(n)):
##    if i<5:
##        print(' '*i+n[i])
##    else:
##        print(' '* (10-i)+n[i])
