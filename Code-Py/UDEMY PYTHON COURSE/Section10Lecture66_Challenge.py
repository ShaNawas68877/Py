'''for i in range(2,13):
    for j in range(1,13):
        tables = ("{1} times {0} is {2}".format(i,j,i*j))


with open('C:\\Users\\Shanawas\\Desktop\\UDEMY PYTHON COURSE\\sample.txt','a') as appended_file:
    print(tables, file=appended_file)'''
#solution

with open('C:\\Users\\Shanawas\\Desktop\\UDEMY PYTHON COURSE\\sample.txt','a') as tables:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i,j,i*j), file=tables)
        print("-"*20, file=tables)
