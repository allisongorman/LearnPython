from sys import argv
from os.path import exists

# argument variables are script, from_file and to_file
script, from_file, to_file = argv

# notify user that program will be copying from from_file to to_file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

# important to close files you are no longer using - OS limits amount of open files you can have
out_file.close()
in_file.close()