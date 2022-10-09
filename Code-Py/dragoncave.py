import random
x = random.randint(1,2)
def displayintro():
    print("This is the intro")
def gamE():
    print("Choose 1 or 2")
    y = int(input())
    if x == y:
        print("Dark cave, you are gonna be eaten")
    else:
        print("You are safe")
playagain = "yes"
while playagain == "yes":
    displayintro()
    gamE()
    print("Do you want to play again?(yes or no)")
    playagain = input()
print("Thanks for playing the game")
