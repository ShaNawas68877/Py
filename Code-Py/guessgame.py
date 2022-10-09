#print("What is your name?")
import random
num = random.randint(1,50)
pname = str(input("What is your name?"))
print("Hi", pname,"I Think a number, you guess it")
guesstaken = 0
for guesstaken in range(10):
    print("Take guess")
    guess = int(input())
    if guess < num:
        print("Too low")
    if guess > num:
        print("High")
    if guess == num:
        print("You got it")
        break
print("Good, you guessed in",guesstaken,"guesses")
if guess != num:
    print("The num i was thinking was",num)
