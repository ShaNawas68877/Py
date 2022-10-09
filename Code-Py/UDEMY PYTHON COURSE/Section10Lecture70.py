#Manipulating data with Shelve
import shelve

#with shelve.open('ShelfTest') as fruit:#will automatically close the file, hence outside the look print(fruit["lemon"]) wont work
fruit = shelve.open("ShelfTest")
######fruit['orange'] = "a sweet, orange, citrus fruit"
######fruit['apple'] = "good for making cider"
######fruit['lemon'] = "a sour, yellow citrus fruit"
######fruit['grape'] = "a small, sweet fruit growing in bunches"
######fruit['lime'] = "a sour, green, citrus fruit"

##print(fruit["lemon"])
##print(fruit["grape"])
##
##fruit["lime"] = "great with tequila"
##
##for snack in fruit:
##    print(snack + ": " + fruit[snack])

####while True:
####    shelf_key = input("Please enter a fruit: ")
####    if shelf_key == "quit":
####        break
####
####    if shelf_key in fruit:
####        description = fruit.get(shelf_key)
####        print(description)
####
####    else:
####        print("Sorry, We dont have a ", shelf_key )

########ordered_keys = list(fruit.keys())
########ordered_keys.sort()
########
########for f in ordered_keys:
########    print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())



fruit.close()

#print(fruit)
