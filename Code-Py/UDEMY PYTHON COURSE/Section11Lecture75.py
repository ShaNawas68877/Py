#Modules and Import
#TurtleDemo
##
##import turtle
##import time
##
##turtle.forward(150)
##turtle.right(250)
##turtle.forward(150)
##turtle.done()
#time.sleep(4)

####from turtle import forward, right, done
####import turtle
####
####forward(250)
####right(250)
####forward(250)
####turtle.circle(75)
####done()
######done = "well done, you have finished your drawing"
######from turtle import *# star will import eveything but its problematic
######forward(250)
######right(250)
######forward(250)
######circle(75)
######done()
######print(done)
#<function mainloop at 0x0000025D2162DC80> Confusion between the object done and user defined done so no star


from turtle import *# star will import eveything but its problematic
done = "well done, you have finished your drawing"
forward(250)
right(250)
forward(250)
circle(75)
done()
print(done)

'''Traceback (most recent call last):
  File "S:/UDEMY PYTHON COURSE/Section11Lecture75.py", line 38, in <module>
    done()
TypeError: 'str' object is not callable

'''
