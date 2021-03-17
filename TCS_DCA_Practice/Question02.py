# Consider 1 element and from there take the next two elements and add all 3 like this do for all elements and give the max sum.

# Take the size of the array as input from console.

# If input elements are less than 4, i.e., size is given less than 4, then print Invalid Input.

# Input 1 - [1, 2, 3, 4, 5]
# Expected Output - 12

# Explaination - 1 + 2 + 3 = 6,
# 				1 + 3 + 4 = 8,
# 				1 + 4 + 5 = 10,
# 				2 + 3 + 4 = 9,
# 				2 + 4 + 5 = 11, 
# 				3 + 4 + 5 = 12. (highest)


# Input 2 - [5, 2, 0, 1, 6]
# Expected Output - 12

import sys

def highest(arr):
	high = -sys.maxsize
	n = len(arr)
	if n < 4:
		return "Invalid Input"
		
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			high = max(high, arr[i] + arr[j] + arr[j + 1])

	return high


array = list(map(int, input().split()))
result = highest(array)
print(result)
