def palindrome(string):
	if not len(string):
		return True
	return string[0] == string[-1] and palindrome(string[1:-1])

max_pal = 0
for i in range(100, 1000):
	for j in range(i, 1000):
		prod = i * j
		if palindrome(str(prod)) and prod > max_pal:
			max_pal = prod
print(max_pal)
			
