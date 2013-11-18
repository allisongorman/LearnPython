# import argv module from sys library
from sys import argv

# argument variable will contain script name and filename
script, filename = argv

# print we are going to delete file with name 'filename'
print "We're going to erase %r." % filename
# print to user that if they do not want to delete enter 'CTRL-C' - this will exit script
print "If you don't want that, hit CTRL-C (^C)."
# print to user if you want to delete hit retun
print "If you do want that, hit RETURN."
# prompt user with question mark for them to select 'CTRL-C' or 'ENTER'
raw_input ("?")
# CTRL-C will exit script and ENTER will continue with script
print "Opening the file..."
# open command requires two parameters - filename and what you want to do to that file
target = open(filename, 'w')

#send message to user that the file is being truncated
print "Truncating the file. Goodbye!"
# truncate file - make it a set size
target.truncate()

# print to user that they will be prompted for three lines
print "Now I'm going to ask you for three lines."

# Enter input for line 1-3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# notify use that thes lines will be written to a file
print "I'm going to write these to the file."
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# using strings, formats and escapes to print out line1, line2, and line3 with just one target.write() command
target.write(line1 + "\n" + line2 "\n" + line3 + "\n")

# notify the user that the file will be closed
print "And finally, we close it."
target.close 