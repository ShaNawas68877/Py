a = float(input("Enter the lenght of the first side"))
b = float(input("Enter the length of the second side"))
c = float(input("Enter the length of the Third side"))
if a >= b + c or b >= c + a or c >= a + b:
    print("Invalid triangle")
else:
    print("It is a valid triangle")
