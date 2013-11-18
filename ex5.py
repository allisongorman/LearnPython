name = 'Allison M. Gorman'
age = 26 
height = 72 # inches
weight = 150 #pounds
centimeters_per_inch = 2.54
kilograms_per_pound = 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

print "Let's convert to the metric system"
print "Her height is %d centimeters." % (height * centimeters_per_inch)
print "Her weight is %d kilograms." % (weight * kilograms_per_pound)
