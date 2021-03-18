# Write a program to find the smallest integer value 'b' for
# the given value of 'a'. If we multiply the digits of 'b', 
# we should get the exact value of 'a'. Result 'b' must contain
# more than one digit.

# Constraints:
# 1  <= a <= 10000

# Examples:
# Input: 10
# Output: 25

# Explaination: 2*5=10. Hence, 25 is the smallest value for 10.

# Input: 56
# Output: 78
# Explaination: 7*8=56

# Input: 150
# Output: 556
# Explaination: 5*5*6

# Input: 13
# Output: Not Possible


def findingSmallest(num):
	if num < 10:
		return num + 10

	temp = []
	for i in range(9, 1, -1):
		while num % i == 0:
			num = num // i
			temp.append(i)


	if num > 10:
		return "Not Possible"

	return int(''.join(map(str, temp[::-1])))


num = int(input())
result = findingSmallest(num)
print(result)
