#Good use of function, Alhamdulillah!

print("""You enter a dark room with three doors.""")

def game():
    print("Please Choose #1 or #2 or #3")
    door = input("> ")

    if door == "1":
        print("There's a giant bear here eating a cheese cake")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")
        print("3. Stand still")

        bear = input("> ")

        if bear == "1":
            print("The bear eats your face off. Good job!")
        elif bear == "2":
            print("The bear eats your legs off. Good job!")
        else:
            print(f"Well, doing {bear} is probably better.")
            print("Bear runs away after a while")

    elif door == "2":
        print("You stare into a beautiful garden full of flowers")
        print("1. Would you stand in awe?.")
        print("2. Or Would you pluck a flower.")

        action = input("> ")

        if action == "1":
            print("Well! You should not pluck flowers")
            print("Good job!")
        else:
            print("A giant monster wakes up and chases You")
            print("Run Away!")

    else:
        print("You enter a dark room again")
        game()
game()
