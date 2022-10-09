d = "Invalid triangle"
e = "It is a valid triangle"

def valid_triangle(a=0, b=0, c=0):

    if a >= b + c or b >= c + a or c >= a + b:
        print(d)
    else:
        print(e)
 
a = float(input("Enter the lenght of the first side"))
b = float(input("Enter the length of the second side"))
c = float(input("Enter the length of the Third side"))
valid_triangle(a, b, c)
