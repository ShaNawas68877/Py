def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just fucntions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 1.5)
iq = divide(225, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a puzzle!")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#divide(iq, 2) =  iq / 2 = (225 / 2) / 2 = 112.5 / 2 = 56.25
#multiply(weight, 56.25) = weight * 56.25 = (90 * 1.5) * 56.25 = 7593.75
#subtract(height - 7593.75) = (74 - 7593.75)
#add(35 + 7593.75) = -7484.75
print("That becomes: ", what, "Can you do it by hand?")
