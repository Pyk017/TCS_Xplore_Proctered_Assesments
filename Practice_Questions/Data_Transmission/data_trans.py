import heapq

def isPrime(num):
	if num == 1:
		return False

	if num == 2 or num == 3:
		return True

	i = 2
	while i * i < num:
		if num % i == 0:
			return False
		i += 1

	return True



numbers = list(map(int, input()[:-1].split()))
result = list(filter(isPrime, numbers))
n = len(result)
heapq._heapify_max(result)
heapq._heappop_max(result)
res = heapq._heappop_max(result)
print(res + n)