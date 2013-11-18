# The variable x is a string with a number
x = "There are %d types of people." % 10
# The variable is a string
binary = "binary"
# The variable is a string
do_not = "don't"
# The variable is a string that contains to string variables (1)
y = "Those who know %s and those who %s." % (binary, do_not)

# Display each string
print x
print y

# Print string with variable x that is a string  (2)
print "I said: %r." %x
# Print string with variable y that is a string (3)
print "I also said: '%s'." %y

# Variable is equal to false
hilarious = False
# Evaluation is dependent on what is chosen for 'r' (4)
joke_evaluation = "Isn't that joke so funny?! %r"

# Print line and value of 'r' is equal to hilarious variable. This variable is false. (5)
print joke_evaluation % hilarious 

# The variable is a string
w = "This is the left side of..."
# The variable is a string
e = "a string with a right side."

# Print strings together (6)
print w + e
