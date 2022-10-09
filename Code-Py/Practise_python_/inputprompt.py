z = str(input("Enter the alphabets"))
'''while len(z) > 10:
    z = str(input("Enter the alphabets"))
print (len(z))
x = z[0:10]
#print (len(x))'''
z = z.lower()
z = z.replace(",","")
z = z.replace(" ","")
x = list (z)
print (x[0:10])
