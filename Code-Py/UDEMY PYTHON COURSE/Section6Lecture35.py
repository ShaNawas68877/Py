#Understanding Continue, Break and Else

##shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
##for item in shopping_list:
##    print("Buy " + item)  


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item is "spam":
        continue
        print("Buy " + item)
