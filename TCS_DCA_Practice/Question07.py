# Take an array of inputs, take size of array as input and determines how many inputs given contain only numbers and how many inputs
# given contain only alphabets.

# If an input contains both alphabets and numbers, then print Invalid Input.

# Input Array - [15, a, 16, ab, 225, 2, 3, teja]
# Ouput - 
# Digits = 5
# Words = 3

# Explanation - In this input, only numbers and words are given, 15, 16, 225, 2, 3 so 5 numers are a, ab, teja so 3 words

# Input Array - [15, a, 16, ab, 225a, 2, 3, teja]
# Ouput -	Invalid Input

# Explanation - In this input, 4 numbers (15, 16, 2, 3) are present and 3 words (a, ab, teja) are present, but this input also contains '225a'
# combination of alphabets and numbers hence Ouput should be given as Invalid Input.


def findingAlphaNumeric(arr):
	digits, words = 0, 0
	for entry in arr:
		if entry.isalpha():
			words +=1
		elif entry.isdigit():
			digits += 1
		else:
			return None

	return (digits, words)



array = list(input().split())
try:
	digits, words = findingAlphaNumeric(array)
	print(f'Digits = {digits}\nWords = {words}')
except:
	print("Invalid Input")