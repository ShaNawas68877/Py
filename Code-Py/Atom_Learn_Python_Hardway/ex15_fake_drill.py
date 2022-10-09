from sys import argv

script, filename = argv

#txt = open(filename)
txt = open(filename).read()

print(f"Here's your file {filename}")
#print(txt.read())
#comment out 5 and 9, and uncomment 6 and 12
#alternate
print(txt)
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
