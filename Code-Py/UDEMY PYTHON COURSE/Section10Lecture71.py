#Updating with Shelve

import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


##with shelve.open('recipes') as recipes:
##    recipes["blt"] = blt
##    recipes["beans_on_toast"] = beans_on_toast
##    recipes["scrambled_eggs"] = scrambled_eggs
##    recipes["pasta"] = pasta

recipes = shelve.open('recipes', writeback=True)

##recipes["soup"] = soup
##recipes["blt"].append("butter")
##recipes["pasta"].append("tomato")

#CANNOT UPDATE THE VALUES DIRECTLY HENCE, CREATING A TEMP LIST

##temp_list = recipes["blt"]
##temp_list.append("butter")
##recipes["blt"] = temp_list
##
##temp_list = recipes["pasta"]
##temp_list.append("tomato")
##recipes["pasta"] = temp_list

#HOWEVER, CAN UPDATE DIRECTLY USING THE WRITEBACK OPTION

#recipes["soup"].append("croutons")

recipes["soup"] = soup
recipes.sync()
soup.append("cream")

for snack in recipes:
    print(snack, recipes[snack])

recipes.close()
