from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

#in_file = open(from_file)

#We have not created a file object, so when this command runs,
#the file will automatically close, so no need to close at the end
indata = open(from_file).read()

print(f"Copying from {from_file} to {to_file}\nThe input file is {len(indata)} bytes long\nDoes the output file exist?\n {exists(to_file)}\nReady, hit RETURN to continue, CTRL+C to abort.")

#print(f"Does the output file exist?\n {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL+C to abort.")
input()

#out_file = open(to_file, 'w')
#We have not created a file object, so when this command runs,
#the file will automatically close, so no need to close at the end
open(to_file, 'w').write(indata)

print("Alright, all done.")

#We have not created a file object, so when this command runs,
#the file will automatically close, so no need to close at the end
#out_file.close()
#in_file.close()
