# Write a program to find the Nth smallest element in the array.

# Example - [30, 15, 10, 5, 80, 2, 56, 150]
# Find - 4th
# 2, 5, 10, 15, 30, 56, 80, 150
# Output - 15

import heapq

def findingNthSmallest(arr, target):
	heapq.heapify(arr)
	for i in range(target - 1):
		heapq.heappop(arr)

	return heapq.heappop(arr)


array = list(map(int, input().split()))
target = int(input())
result = findingNthSmallest(array, target)
print(result)