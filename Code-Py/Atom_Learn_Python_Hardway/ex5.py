name = 'Shanawas'
age = 25
height = 67
height_in_cm = height * 2.54
weight = 65
weight_in_pounds = weight * 2.205
eyes = 'Brown'
teeth = 'white'
hair = 'Black'

#print(f"Let's talk about {name}.")
print("Let's talk about {}.".format(name))
print(f"He's {height_in_cm} centimeters tall.")
print(f"He's {weight_in_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")
