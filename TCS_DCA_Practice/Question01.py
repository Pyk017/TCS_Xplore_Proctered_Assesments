# Take string as an input from console and remove 8 and 53 from the string and give back the output string with all the characters in 
# the string in lowercase.

# If the given input doesnot contains all the characters as alphabets or number, then print "Invalid input given, please remove the 
# characters that are non digits and alphabets".

# Input 1 - AB5HJ53JK8LP
# Expected Ouput - ab5hjjklp

# In the above scenario, Input contains 53 and 8, hence they are removed and the remaining part of the string is given back.

# Input 2 - ABJK8KLP
# Expected Ouput - abjklp

# Input 3 - ABJK%LP
# Expected Output - "Invalid input given, please remove the characters that are non digits and alphabets"

# In the above scenario, Input contains %, hence error message is given.


import re

def removeCharacters(string):
	for char in string:
		if not char.isalnum():
			return 'Invalid input given, please remove the characters that are non digits and alphabets'

	while '53' in string or '8' in string:
		string = string.replace('53', '')
		string = string.replace('8', '')
	return string.lower() 	


string = input()
result = removeCharacters(string)
print(result)