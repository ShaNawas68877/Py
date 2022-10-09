#Test Conditions With If, Elif and Else

name = input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
print(age)

#Converting age into int, so that we can do int processing-------------------------------------

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age>= 18:
    print("You are old enough to vote") #if left with if itself, nothing will happen when the condition fails
    print("Please put an X in the ballot box")
else:
    print("Please come back in {0} years".format(18-age))

#For more than two cases--------------------------------------

print("Please guess a number between 1 and 10")
guess = int(input())

if guess<5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")
elif guess>5:
    print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

#Efficient code because the above code has repetitions--------------

print("Please guess a number between 1 and 10")
guess = int(input())

if guess != 5:
    if guess <5:
        print("Please guess higher")
    else:
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("sorry, you have not guessed correctly")
else:
    print("you got it first time")
