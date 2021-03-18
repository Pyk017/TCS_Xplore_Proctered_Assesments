# Take a string as input and determine whether the first character is uppercase or lowercase or digit or symbol.

# Input - Prakhar
# Output - UPPERCASE

# Input - %hai
# Output - symbol

import string

def findingFirstChar(inp_str):
	if inp_str[0] in string.ascii_uppercase:
		print("UPPERCASE")
	elif inp_str[0] in string.ascii_lowercase:
		print("lowercase")
	elif inp_str[0] in string.digits:
		print('Digit')
	else:
		print("symbol")


inp_string = input()
findingFirstChar(inp_string)