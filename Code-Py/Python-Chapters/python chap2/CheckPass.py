def CheckPass(password):
    has_upper = False
    has_lower = False
    has_number = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        if ch >= "a" and ch<= "z":
            has_lower = True
        if ch >= "0" and ch <= "9":
            has_number = True
    if len(password) >= 8 and has_upper and has_lower and has_number:
        return True
    else:
        return False
def main():
    p = input("Enter the password:")
    if CheckPass(p):
        print("good")
    else:
        print("bad")
main()
        





