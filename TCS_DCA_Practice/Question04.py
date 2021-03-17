# Take two strings as an input.

# Find the common characters between the strings and give back the output.

# Arrange the identified characters in alphabetic orders as well as reverse order.

# Input 1 - hai
# Input 2 - hola

# Expected Output 
# Normal Order - [a, h]
# Reverse Order - [h, a]


def commonCharacters(str1, str2):
	res = []
	for char in list(set(str1)):
		if char in str2:
			res.append(char)

	return (res, res[::-1])


string1 = input()
string2 = input()
normal, reverse = commonCharacters(string1, string2)
print(f'Normal Order - {normal}')
print(f'Reverse Order - {reverse}')

