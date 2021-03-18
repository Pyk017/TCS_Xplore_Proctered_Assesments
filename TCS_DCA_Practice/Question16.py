# John and Linda are playing a number game, John asked Linda to find the number
# whose square ends with the number itself. The number should also be a positive
# integer. Write a program to implement the above logic.

# Input Format:
# Input contains an integer 'N' denoting the number.

# Output Format:
# If the number whose square ends with the number itself, print "Correct Number", 
# otherwise print 'Incorrect Number'. If the user enters negative integer, the 
# result should display "Wrong Input".

# Constraints:
# 1 <= N <= 10^8

# Sample 1:
# Input: 
# 5
# Output:
# Correct Number

# Sample 2:
# Input:
# 9
# Output:
# Incorrect Number

# Sample 3:
# Input: 
# -6
# Output:
# Wrong Input


def findingSimilarNumber(num):
	if num < 0:
		return "Wrong Input"
	elif num == 0:
		return 0
	lenOfNum = len(str(num))
	numSquare = str(num**2)
	return "Correct Number" if numSquare[-lenOfNum:] == str(num) else "Incorrect Number"
	
	


num = int(input())
result = findingSimilarNumber(num)
print(result)
