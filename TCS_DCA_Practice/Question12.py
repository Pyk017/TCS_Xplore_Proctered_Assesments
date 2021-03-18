# Take a number and check if square of the number ends with the same number.

# Input - 15
# Output - Yes
# Explaination - square of 15 => 225 both are ending with digit 5

# Input - 6
# Output - Yes

# Input - 13
# Output - No

# Input - 5
# Output - Yes

def endingSameDigit(num):
	return 'Yes' if str(num)[-1] == str(num**2)[-1] else 'No'

num = int(input())
result = endingSameDigit(num)
print(result)
