# A traveler wants to start his/her journey from Pune
# to Ahmedabad. Before starting the journey, he/she uses
# the GPS system to find all the paths to reach from 
# the source to the destination. He/she will use the
# smallest or the second smallest path to start the journey.
# Write a logic to find the smallest and the second 
# smallest distance from the list of all distances.

# Input:
# 1. The first input contains N, the total number of paths
# from source to the destination.
# 2. The second input contains N sorted integers separated
# by newline A1,A2...An, representing the distance of all
# paths.

# Output contains two numbers separated by a single space character.
# If all paths are equal. then the system should generate a message
# as "Equal".
# If N is less than 2, then the system should generate a message as
# "Invalid Input".

# Constraints:
# 2 < N <= 10
# 1 <= A[i] <= 1000

# Example 1:
# Input:
# 4 
# 100
# 400
# 300
# 250
# Output: 
# 100 250
# Explaination: 
# Out of the 4 possible paths, only 100 and 250 are the 
# smallest distances to reach the destination.

# Example 2:
# Input:
# 1
# 200
# Output:
# Invalid Input
# Explaination:
# In the given constraints, the first value must be greater
# than 2.

# Example 3:
# Input:
# 3
# 100
# 100
# 100
# Output:
# Equal

import heapq

def findingLastTwoSmallest(arr):
	if len(arr) == 1:
		return "Invalid Input"

	elif (len(set(arr)) == 1):
		return "Equal"

	elif len(arr) == 2:
		return arr

	else:
		arr = list(set(arr))
		heapq.heapify(arr)
		result = [heapq.heappop(arr) for _ in range(2)]
		return result


array = list(map(int, input().split()))
result = findingLastTwoSmallest(array)
print(result)