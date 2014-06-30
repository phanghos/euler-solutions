def collatz(n):
	aux = n
	c = 1
	while n != 1:
		if n in lengths:
			lengths[aux] = c + lengths[n] - 1
			return lengths[aux]
		if n % 2 == 0:
			n //= 2
		else:
			n = 3 * n + 1
		c += 1
	lengths[aux] = c
	
	return c
		
def max_length(n):
	max_n = 1
	max_len = 1
	for i in range(1, n):
		l = collatz(i)
		if l > max_len:
			max_n = i
			max_len = l
			
	return max_n
	
lengths = {}
print(max_length(1000000))
