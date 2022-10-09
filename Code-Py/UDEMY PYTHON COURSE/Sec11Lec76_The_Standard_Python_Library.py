#The Standard Python Library
##print(dir())#__ means private to a module
###print(dir(__builtins__))
##for m in dir(__builtins__):
##    print(m)

import shelve
####print(dir())
####for m in dir(shelve):
####    print(m)
######
######for obj in dir(shelve.Shelf):
######    if obj[0] != '_':
######        print(obj)

help(shelve)

import random
help(random.randint)
