# Take a number as input, multiply all digits in the number and give back the output product.

# If the input given is a negative number then give back the output as Number is not valid, please enter a positive number.

# Input 1 - 123
# Output - 6
# Explaination - 1 * 2 * 3 = 6

# Input 2 - -1234
# Output - Number is not valid, please enter a positive number

from functools import reduce
from operator import mul     # using operator.mul()

# def prod(a, b): using user defined function
# 	return a * b

# prod = lambda x, y: x * y   Using lambda function

def multiply(num):
	num = list(map(int, list(str(num))))
	return reduce(mul, num)


Number = int(input())
result = multiply(Number)
print(result)
