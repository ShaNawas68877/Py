a = int(input("Enter the variable: "))
b = int(input("Enter the variable: "))

def while_func(a, b):

    i = 0
    numbers = []

    #while i < a:
    for i in range(0, a, b):
        print(f"At the top i is {i}")
        numbers.append(i)

#        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

while_func(a, b)
