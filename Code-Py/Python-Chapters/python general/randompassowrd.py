from random import randint
short = 7
long = 15
minascii = 33
maxascii = 126
def randomPass():
    randomLen = randint(short, long)
    result = ""
    for i in range(randomLen):
        randomChar = chr(randint(minascii, maxascii))
        result = result + randomChar

    return result
def main():
    print("your random password is:", randomPass())
if __name__ == "__main__":
    main()
                         
