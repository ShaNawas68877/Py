name = input("Please enter your name: ")
age = int(input("Please enter your age {0} ".format(name)))
if 18 < age < 31:
    print("Welcome to the holiday {0}".format(name))
else:
    print("We are sorry {0}, you cannot go for a holiday".format(name))