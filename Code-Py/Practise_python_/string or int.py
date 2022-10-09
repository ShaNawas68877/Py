
def main():
    string = str(input("Please enter the string: "))
    resu = isInteger(string)
    print(resu)

def isInteger(string):
    if len(string) == 0:
        a = "its an integer"
    elif len(string) > 0: #or len(string)[0] == "+" or len(string)[0] == "-":
        a = "its not an integer"
    return a
main()
    
