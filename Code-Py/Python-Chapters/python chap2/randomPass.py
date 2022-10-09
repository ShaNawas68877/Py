import random
def RandomPass():
    randomLen = random.randint(7,10)
    result = ""
    for i in range(randomLen):
        randomChr = chr(random.randint(33,126))
        result = result + randomChr
    return result        
def main():
    print("your random password is:", RandomPass())
if __name__ == "__main__":
    main()
