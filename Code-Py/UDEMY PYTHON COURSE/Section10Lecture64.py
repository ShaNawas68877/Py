#Reading and Writing text files

#Reading text file
#open the file #Reading the file (1 line or whole) #closing the file
'''jabber = open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') # r for read
for line in jabber:
    print(line)

jabber.close()

'''
'''

jabber = open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') # r for read
for line in jabber:
    if "jabberwock" in line.lower(): #lower case
        print(line, end='')

jabber.close()

'''
'''

with open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') as jabber: #with closes the file so no need to close separately
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')


with open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()
'''
'''
#converting the text into list first
with open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines:
    print(line, end='')

'''
'''
#Reversing the lines

with open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]:
    print(line, end='')
'''
#reversing each and every letter
with open("C:\\Users\\Shanawas\\Desktop\\Section10Lecture64_resource.txt",'r') as jabber:
    lines = jabber.read()
print(lines)
for line in lines[::-1]:
    print(line, end='')
