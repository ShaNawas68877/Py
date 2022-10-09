# Exercise 66 : Compute a GPA
gra = str(input('Please enter your grades (blank to finish):'))
while gra != "":
    grade = str(gra)
if grade == "A+" or grade == "A":
    print('Your grade is 4.0')
elif grade == "B" or grade == "B+" or grade == "B-":
    print('your grade is 3.0')
