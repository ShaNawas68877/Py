# Exercise 38 : Month Name to Number of Days
month = str(input("Enter the name of the month: "))
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print('The number of days in', month,'is 31')
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("The number of days in", month,"is 30")
elif month == "February":
    print("The number of days in", month,"is 28 or 29!")
else:
    print("Error : Entered Invalid data")
