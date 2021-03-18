# Take two numbers as input.

# Print the unique digits within the given range.

# Input = 10 15
# Output = 0 2 3 4 5

# Explaination - 10 11 12 13 14 15
# Unique Digits - 0 2 3 4 5


# Input = 100 105
# Output = 2 3 4 5

# Explaination - 100 101 102 103 104 105
# Unique digits - 2 3 4 5


from collections import Counter

def findingUnique(low, high):
	temp_str = ''
	for num in range(low, high + 1):
		temp_str += str(num)

	res = []
	d = dict(Counter(temp_str))
	for item, count in d.items():
		if count == 1:
			res.append(int(item))

	return res



low, high = map(int, input().split())
result = findingUnique(low, high)
print(*result)
