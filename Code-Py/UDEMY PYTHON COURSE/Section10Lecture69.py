#Shelves
import shelve
'''
with shelve.open('ShelfTest') as fruit:#will automatically close the file, hence outside the look print(fruit["lemon"]) wont work
fruit = shelve.open("ShelfTest")
    fruit['Orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green, citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
print(fruit)
'''

'''
#with shelve.open('ShelfTest') as fruit:#will automatically close the file, hence outside the look print(fruit["lemon"]) wont work
fruit = shelve.open("ShelfTest")
fruit['Orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green, citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])
print(fruit)
fruit.close()

print(fruit)
'''

##with shelve.open("bike") as bike:
##    bike["make"] = "Honda"
##    bike["model"] = "250 dream"
##    bike["colour"] = "red"
##    bike["engine_size"] = 250
##
##    print(bike["engine_size"])
##    print(bike["colour"])


#important aspect of Shelve
    #Typo stays in Database

#Explained here
##
##with shelve.open("bike2") as bike:
##    bike["make"] = "Honda"
##    bike["model"] = "250 dream"
##    bike["colour"] = "red"
##    #bike["engin_size"] = 250
##    bike["engine_size"] = 250
##
##    print(bike["engin_size"])#once executed even the incorrect typo key gets saved in the DB
##    print(bike["engine_size"])
##    print(bike["colour"])
##
##with shelve.open("bike2") as bike:
##    
##    for key in bike:
##        print(key)
##
##    print('='*40)
##
##    print(bike["engine_size"])
##    print(bike["engin_size"])
##    print(bike["colour"])


with shelve.open("bike2") as bike:
    del bike["engin_size"]#Deleting the typo key from DB
    
    for key in bike:
        print(key)

    print('='*40)

    print(bike["engine_size"])
    #print(bike["engin_size"])
    print(bike["colour"])


