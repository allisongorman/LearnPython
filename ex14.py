from sys import argv

script, user_name, age = argv
prompt = '->'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name 
likes = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Is %s a fun place for %s year olds?" % (lives, age)
fun = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You said %r to whether where you live is a fun place for %r year olds.
And you have a %r computer. Nice.
""" % (likes, lives, fun, age, computer)
