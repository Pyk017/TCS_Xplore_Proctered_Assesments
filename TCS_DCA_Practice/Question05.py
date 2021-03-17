# Take an array of integers as input

# Take size from console.

# Add up all elements in the ascending order of their presence and give back the final output.

# Input 1 - [2, 201, 2, 3, 200, 4, 5]
# Output - [203, 205, 9]
# Explaination - 	2 + 201 = 203
# 				2 + 3 + 200 = 205
# 				4 + 5 = 9

# Input 2 - [15, 10, -2, 200, 4, 5]
# Output - [198, 9]   ([15, 10] are in descending order thus cannot be added).


def addition(arr):
	res = []
	i = 0
	j = 0
	while arr[j] > arr[j + 1]:
		j += 1

	temp = arr[j]
	i = j 

	while i < len(arr) - 1:
		if arr[i] <= arr[i + 1]:
			temp += arr[i + 1]
			i += 1
		else:
			res.append(temp)
			temp = arr[i + 1]
			i += 1

	res.append(temp)
	return res


array = list(map(int, input().split()))
result = addition(array)
print(result)