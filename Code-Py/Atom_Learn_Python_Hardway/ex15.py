from sys import argv

#Giving the parameters in the command line itself instead of input
script, filename = argv

#Creating fileobject which holds the file
txt = open(filename)

#printing the filename
print(f"Here's your file {filename}")
#printing the file content
print(txt.read())
#closing the opened file, if we try to run the 12th line again, will
#receive an error, since the file is closed
txt.close()
#print(txt.read())

print("Type the filename again:")
#getting the file name again
file_again = input("> ")
#creating a fileobject for this new file or closed previous file
txt_again = open(file_again)
#printing it
print(txt_again.read())
#closing it
txt_again.close()
