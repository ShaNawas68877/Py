n = ''
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
           print(p[j][i],end='')
        else:
           print(p[j][i])
