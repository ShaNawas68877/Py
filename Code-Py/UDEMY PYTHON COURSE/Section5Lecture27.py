#String Formatting - Displaying Numbers and Strings

#numbers cannot be concatenated or appended with string using plus operator

'''
age = 24
print("My age is " + age + "years") #error must be str not int because we are trying to append int to string
'''

#----------------------------------------
#correction
age = 24
print("My age is " + str(age) + " years")

#-----------------------------------------

print("My age is {0} years".format(age))

#Concept of replacement fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March", "May", "July",
                                                                           "August", "October", "December"))
#-----------------------------------------

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31)) #3 double quotes to type within quotes in multiple lines

#---------------------------------------
'''
print("January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}".format(28, 30, 31))
'''

#--------------------------------------

#String formatting operator - not used in python3

print("My age is %d years" % age) #python2
print("My age is {0} years".format(age)) #python3
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))#python2
print("My age is {0} {1}, {2} {3}".format(age, "years", 6, "months"))#python3

#-------------------------------------


for i in range(1,12):
    print("No, %2d squared is %4d and cubed is %4d" %(i, i**2, i **3)) # 2d, 4d is for space allocation not to look messy, below example shows it
 
#Messy arrangement example removing 2 and 4 between d------------

for i in range(1,12):
    print("No, %d squared is %d and cubed is %d" %(i, i**2, i **3)) # 2d, 4d is for space allocation not to look messy, below example shows it

print("pi is approximately %12f" % (22/7))
print("pi is approximately %12.50f" % (22/7))

#Replacement field with space allocation---------

for i in range(1,12):
    print("No, {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i **3)) # {0:2} {1:4} {2:4} is for space allocation not to look messy, below example shows it

print("pi is approximately {0:12.50}".format(22/7))

#REPLACEMENT FIELD NEED NOT BE IN ORDER WE CAN USE NUMBER INSTEAD IF NO NUMBER THEN IT TAKES AS IN ORDER

print("January:{}, February: {}, April: {}".format(31, 28, 30))
print("January:{0}, February: {2}, April: {1}".format(31, 28, 30))
