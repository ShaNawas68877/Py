age = 23
print("my age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "JAN", "MAR", "MAY", "JUL", "AUG", "OCT", "DEC"))
print("""Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1} """.format(28, 30, 31))

print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
for i in range (1,12):
    print("No %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

for i in range (1,12):
    print("No {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3))

for i in range (1,12):
    print("No %d squared is %4d and cubed is %d" %(i, i ** 2, i ** 3))#if no %2d and %4d, bad formatting

print("pi is approximately %12.50f"%(22/7))
print("pi is approximately %12f"%(22/7))