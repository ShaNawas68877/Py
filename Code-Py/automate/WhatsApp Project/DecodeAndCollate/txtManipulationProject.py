##with open('kgf movie name.txt', 'r') as reader:
##    print(reader.read())
##
##with open('kgf movie name.txt', 'r') as reader:
##    print(reader.readline(5)) #reading just 5 bytes
##
###READING ENTIRE LINE AS A LIST
##
##f = open('kgf movie name.txt')
##print(f.readlines())


#ITERATING OVER LINES
##with open('gandhi.txt', 'r') as reader:
##    for line in reader:
##        print(line)

#WRITING (A NEW FILE?) reversed line using space
##with open('gandhi.txt', 'r') as reader:
##    gandhi = reader.readlines()
##with open('reversed_gandhi.txt', 'w') as writer:
##    for line in reversed(gandhi):
##        writer.write(line)
#APPENDING TO THE EXISTING FILE

##with open('gandhi.txt', 'a') as appender:
##    appender.write('whatever in the end')


##with open('gandhi.txt','r') as reader:
##    gandhi = reader.read()
##    if('nationalit' in gandhi):
##        print('yes')
##    else:
##        print('no')


## OPENING A FILE, REPLACING FEW WORDS, CREATING A NEW FILE AND PASTING THE NEW REPLACED WORDS IN THE NEW FILE
with open('gandhi.txt', 'r') as reader:
    gandhi = reader.read()
    print(type(gandhi))
    gandhi1 = gandhi.replace('nationalist','')
with open('gandhi2.txt', 'w') as writer:
    writer.write(gandhi1)
