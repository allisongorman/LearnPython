# import argv module from sys library
from sys import argv

# argument variable will hold the script and filename arguments
script, filename = argv

# txt variable will have the contents of filename 
txt = open(filename)

# print to screen the filename
print "Here's the file you created %r:" % filename
# print to screen the text of txt
print txt.read() 		

# request user to type in the filename
print "Type the filename again:"
# variable 'file_again' will take in typed input
file_again = raw_input("> ")

# txt_again variable will have the contents of file_again
txt_again = open(file_again)

# print to screen the text contents of 'txt_again'
print txt_again.read()