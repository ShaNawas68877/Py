from sys import argv
#Tring only the input part
#Trying only the argv part
"""
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())
"""
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close() #txt_again is the fileobject
                    #We need to give fileobject.close() to close the
                    #opened file
"""
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
"""
