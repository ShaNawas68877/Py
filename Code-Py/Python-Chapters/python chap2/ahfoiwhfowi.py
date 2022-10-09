def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return a
    if c < b and c > a or c > b and c < a:
        return c
def alternateMedian(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))
    print("The median value is : ", median(x, y, z))
    print("using the alternative method, it is: ", alternateMedian(x, y, z))
main()


