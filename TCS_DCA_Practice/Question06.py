# Take a string as input

# Find the number of ways the string can be arranged, when all the vowels are together.

# Note - Handle both repetition and non-repetition scenario as well.

# Input 1 - Sister
# Output - 120

# Input 2 - Animation
# Output - 1800


from collections import Counter
from functools import reduce
from math import factorial as fact

def repetition(string):
	vowels, consont = 0, 0
	for char in string:
		if char in 'aeiouAEIOU':
			vowels += 1
		else:
			consont += 1

	repeat = list(filter(lambda x: x > 1, dict(Counter(string)).values()))
	deno = 1
	for num in repeat:
		deno *= fact(num)

	numerator = fact(vowels) * fact(consont)

	return numerator // deno


string = input()
result = repetition(string)
print(result)