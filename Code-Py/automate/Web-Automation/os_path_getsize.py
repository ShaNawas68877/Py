import os
totalSize = 0
n = os.path.getsize("C:\\Users\\Shanawas\\Desktop\\learn liist.py")
for filename in os.listdir("C:\\Users\\Shanawas\\Desktop"):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Shanawas\\Desktop', filename))
#print(totalSize//(1024*1024))
helloFile = open('C:\\Users\\Shanawas\\Desktop\\learn liist.py')
print(helloFile)
