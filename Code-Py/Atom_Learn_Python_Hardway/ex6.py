types_of_people = 10
#embedding the variable types_of_people in this string
x = f"There are {types_of_people} types of people"
#variable declaration
binary = "binary"
do_not = "don't"
#String inside a string
#embeds binary variable and do_not variable in this string
y = f"Those who know {binary} and those who {do_not}."

#prints x
print(x)
#prints y
print(y)
#String inside a string
print(f"I said: {x}")
#String inside a string
print(f"I also said: '{y}'")
#Declaring a variable
hilarious = False
#Declaring a variable with a String
joke_evaluation = "Isn't that joke so funny?! {}"
#printing the joke_evaluation variable with embedding hilarious variable as a string formatting feature
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
# printing by concatenating w variable and e variable
print(w + e)
