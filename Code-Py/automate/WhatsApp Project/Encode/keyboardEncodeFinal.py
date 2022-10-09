kb1 = ['q' ,'w' ,'e' ,'r' ,'t' ,'y' ,'u' ,'i' ,'o', 'p']
kb2 = ['a','s','d','f','g','h','j','k','l']
kb3 = ['z','x','c','v','b','n','m']
kb4 = [',','!','?',"'"]

kb5 = 'dont know why, but i like when you say seruppu'
kb5 = kb5.lower()

output = []
for i in range(0, len(kb5)):
    if kb5[i] in kb1:
        m = 9 - (kb1.index(kb5[i]))
        output.append(kb1[m])
    elif kb5[i] in kb2:
        n = 8 - (kb2.index(kb5[i]))
        output.append(kb2[n])
    elif kb5 [i] in kb3:
        o = 6 - (kb3.index(kb5[i]))
        output.append(kb3[o])
    elif kb5 [i] in kb4:
        output.append(kb5[i])
    else:
        output.append(' ')

FinOut = ''.join(output)
print(FinOut)
