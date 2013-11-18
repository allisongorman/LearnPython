# Print to the screen that we are about to count chickens
print "I will now count my chickens:"

# Number of hens is 25 + (30/6 = 5) = 30
print "Hens", 25 + 30 / 6
# Number of roosters is 100 - (25X3) modulo 4 (what is leftover after dividing by 4)
print "Roosters", float(100) - float(25) * float(3) % float(4)

print "Now I will count the eggs:"

# Number of eggs is 3+2+1-5+(4%2=0)-(1/4=0)+6
print 3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2



