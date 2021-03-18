# Create the following series:

# Take the input integers, and give back the value present at that position.

# The series is: 0 0 2 1 4 3 6 5 8 7 10 9 ...


def findingNumber(num):
	if num == 1 or num == 2:
		return 0
	return num - 1 if num & 1 else num - 3

num = int(input())
for i in range(1, num + 1):
	print(findingNumber(i), end=' ')

print()
result = findingNumber(num)

print(result)