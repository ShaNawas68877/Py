age = int(input("How old are you?"))
# # if (age >= 16) and (age <=65):
# if 16 <= age <= 65:
#     print("Have a good day at work")

if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")

x = input("please enter some text ")
if x:
    print("you entered '{}'".format(x))
else:
    print("You entered nothing")

print(not False)
print(not True)

parrot = "Norwegian blue"
letter = input("Enter a character")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I dont need that letter")