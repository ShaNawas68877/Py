#Number of cars is 100
cars = 100
#The amount of space for the passengers to sit is given as 4
space_in_a_car = 4.0
#Number of drivers is 100
drivers = 30
#Number of passengers is 100
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transpost", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
