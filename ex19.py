# function cheese_and_crackers takes two paramaters: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print the amount of cheeses, boxes of crackers, that we should have a party and to bring a blanket 
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
# this example shows how you can input numbers directly into the funciton
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# this example creates two variables that are used as parameters for the function 
print "Or, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# number of cheese and crackers is calculated within the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# number of cheese is calculated with math using variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


