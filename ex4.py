# Number of cars
cars = 100

# Number of passengers a car can hold
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Number of cars not driven is number or cars minus number of drivers
cars_not_driven = cars - drivers

# Number of cars driven is equal to drivers
cars_driven = drivers

# Number of people that can carpool is number of cars plus the space in the car
carpool_capacity = cars_driven + space_in_a_car

# Number of pasengers per car is the average of passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

