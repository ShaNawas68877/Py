from sys import argv

script, filename = argv

print(f"We are going to read the {filename}")

trunc = open(filename)
print(trunc.read())
trunc.close()
