from random import randint
def randomPass(v):
    #randomLen = randint(5,15)
    result = ""
    for i in range(v):
        randomChar = chr(randint(33,126))
        result = result + randomChar
    return result
def main():
    v = int(input("Please enter the length"))
    print("your randompassword is", randomPass(v))
    Yourpass = input("Please enter your password:")
    print(Yourpass)
main()
