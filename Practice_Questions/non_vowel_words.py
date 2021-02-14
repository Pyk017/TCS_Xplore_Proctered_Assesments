def nonVowelWords(string):
	for char in string:
		if char in 'aeiou':
			return True

	return False


if __name__ == '__main__':
	n = int(input())
	string_list = []
	for _ in range(n):
		string_list.append(input())

	result = list(filter(nonVowelWords, string_list))
	if result:
		for string in result:
			print(string)
	else:
		print("No words are there without vowels")