kb1 = ['q' ,'w' ,'e' ,'r' ,'t' ,'y' ,'u' ,'i' ,'o', 'p']
kbs = 'qwertyuiop'
kb2 = ['a','s','d','f','g','h','j','k','l']
kb3 = ['z','x','c','v','b','n','m']
kb4 = [',','!','?']
test = 'have a great sleep'

outp1 = []
outp2 = []
outp3 = []
output = []
for i in range(0, len(test)):
    if test[i] in kb1:
##        print(kb1.index(test[i]))
        m = 9 - (kb1.index(test[i])) #number of elements in kb1 minus 1 is m
##        print(m)
##        print(kb1[m])
        output.append(kb1[m])
##        outp1.append(kb1.index(test[i]))
    elif test[i] in kb2:
##        print(kb2.index(test[i]))
        n = 8 - (kb2.index(test[i]))
        ##        print(n)
##        print(kb1[n])
        output.append(kb2[n])
##        outp2.append(kb2.index(test[i]))
    elif test [i] in kb3:
        print(kb3.index(test[i]))
        o = 6 - (kb3.index(test[i]))
        ##        print(o)
##        print(kb1[o])
        output.append(kb3[o])
    elif test [i] in kb4:
##        print(kb3.index(test[i]))
##        o = 6 - (kb3.index(test[i]))
        ##        print(o)
##        print(kb1[o])
        output.append(test[i])
    else:
        output.append(' ')
        
##print(output)
##print(kb1[outp1])
##print(outp2)
##print(outp3)
##output = outp1+outp2+outp3
##print(str(output))

FinOut = ''.join(output)
print(FinOut)
