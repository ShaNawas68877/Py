import random
r = 0
lst = random.sample('abcdefghijklmnopqrstuvwxys', 5)
print(lst)
print()
z = str(input("Enter letters (a-z)"))
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
users = list(z)
users = users[0:10]
print (users) 
print("")
print(''.join(map(str, users)))
out = (set(users[0:10]) & set(lst))
out = list(out)
print (out)
print(''.join(map(str, out)))
out = out[:]
indices = [users.index(i) for i in out]
print(indices)


'''
i = out
j = users
while i == j:
    print(i)'''
'''r = 1
j=0
t=[]
for r in (indices):
    #indices[r] = users[r]
    print(users[r])
#print('''










#indices = [users.index(i) for i in out]
#print (indices)
#for i in indices:
    

'''def findInstances(list1, list2):
    """For each item in list1,
    return a list of offsets to its occurences in list2
    """

    for i in list1:
        yield [pos for pos,j in enumerate(list2) if i==j]

res = list(findInstances(users, out))
print (res)
if res == "[0]"
print'''
'''
for i in users:
    i = list(i)
    print (i)
    if i == out:
        print (i)'''

'''for j in out:
    j = list(j)
    if i == j:
        print (i)'''
        
    
'''
    for j in out:
        if users[i] == out[j]:
            i = list(i)
            out = out.pop(i)
            print(out)'''
