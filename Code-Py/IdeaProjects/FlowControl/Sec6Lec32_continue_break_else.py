# shopping_list = ['milk','paste','eggs','spam','bread','rice']
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print('Buy'+item)
#
# shopping_list = ['milk','paste','eggs','spam','bread','rice']
# for item in shopping_list:
#     if item == 'spam':
#         print('I am ignoring', item)
#         continue
#     print('Buy'+item)
#
# shopping_list = ['milk','paste','eggs','spam','bread','rice']
# for item in shopping_list:
#     if item == 'spam':
#         break
#     print('Buy'+item)

meal = ['egg','tomato','spam','sausages']
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:#Learn ELSE
    print("I'll have that, then, please")

if nasty_food_item == 'spam':
    print("cant i have anything without spam")



