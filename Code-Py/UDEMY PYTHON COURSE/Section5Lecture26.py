#More About Variables and Strings

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0]) #Most of the programming languages starts index from 0
print(parrot[3])
print(parrot[-1])#prints backwards
print(parrot[0:6])#prints fro 0 char to 6
print(parrot[:6])# same as previous
print(parrot[6:])# 6 to end
print(parrot[-4:-2])# STARTS FROM 4TH CHARACTER FROM THE END BUT STOPS AT 0 -1 -2
print(parrot[0:6:2]) #starting from 0 to 6 but skip 2 each time
print(parrot[0:6:3]) # starts from 0 to 6 ut skip 3 each time

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = "1,2,3,4,5,6,7,8,9"
print(number[0::3])
string1 = "he's"
string2 = "probably"
print(string1 + string2)
print("he's probably pining")


#Multiplying strings

print("Hello" * 5 )
#print("Hello" * 5 + 4)
today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in today)
