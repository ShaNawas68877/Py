kb1 = ['q' ,'w' ,'e' ,'r' ,'t' ,'y' ,'u' ,'i' ,'o', 'p']
kbs = 'qwertyuiop'
kb2 = ['a','s','d','f','g','h','j','k','l']
##kb3.0 = 'zxcvbnm'
kb3 = ['z','x','c','v','b','n','m']
##for i in range(0,len(kb3)):
##    print('\''+kb3[i]+'\''+',',end='')kb3.0 and for loop to form kb3


##print(type(kb1))
##print(kb1)
##print(kb1[0])
##print(kbs[0])
##s = kb3[1:3]
##print(s)
##print(str(s))
##
##if 'q' in kbs:
##    print('s')

##kb = 'wh'
##if(kb[0] in kb1):
##    if(kb[0] in kb[0,4]):..

test = 'what'
outp1 = []
outp2 = []
outp3 = []
for i in range(0, len(test)):
    if test[i] in kb1:
        print(kb1.index(test[i]))
        outp1.append(kb1.index(test[i]))
    elif test[i] in kb2:
        print(kb2.index(test[i]))
        outp2.append(kb2.index(test[i]))
    elif test [i] in kb3:
        print(kb3.index(test[i]))
        outp2.append(kb3.index(test[i]))
        
print(outp1)
print(kb1[outp1])
print(outp2)
print(outp3)
output = outp1+outp2+outp3
print(output)

