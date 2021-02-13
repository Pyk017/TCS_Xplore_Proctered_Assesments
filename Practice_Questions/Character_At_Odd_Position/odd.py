string = list(input())
result = ''
for x in range(1, len(string), 2):
	result += string[x]

print(result)