#Exercise 5 : Bottle Deposits

num = int(input('Enter the number of 1 litre containers you have:'))
num2 = int(input('Enter the number of more than 1 litre containers you have:'))
refund = num * 0.10 + num2 * 0.25
print('your total refund will be $'+format(refund,'.2f'))#ufff, atlast format specifier got it. the old format specifier is %.2f
                                                         #new format is above used.
#for num in range (1,num):
   # containersize = float(input('Enter the container size:'))
   # if containersize <= 1:
    #    deposit = 0.10*num
   # else:
   #     deposit = 0.25*num
#print('$')
        
    


