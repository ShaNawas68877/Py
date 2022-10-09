n = 'I thought "LOVE" is love but just realised its just U'
m = len(n)/2
o = int(float(m))
##print(o)
for i in range(0,len(n)):
    if i<o:
        print(' '*i+n[i])
    else:
        print(' '* ((o*2)-i)+n[i])
