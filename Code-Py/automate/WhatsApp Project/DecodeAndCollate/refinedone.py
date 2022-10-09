with open('english3.txt', 'r') as ding:
    engd = ding.read()
    engdlist = engd.split()

with open('3-19-20.txt', 'r', encoding='ascii', errors='surrogateescape') as reader:
    gandhi = reader.read()
    gandhilist = gandhi.split()
    
##    print(gandhilist)

with open('refinedemo.txt', 'w') as writer:
    b = []
    for a in gandhilist:
        a.upper()
        if a not in engdlist:
            b.append(a)

    c = ' '
    d = c.join(b)
    writer.write(d)
