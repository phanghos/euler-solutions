def prime(n):
	if n % 2 == 0: return False
	end = int(n ** .5)
	for i in range(3, end + 1, 2):
		if n % i == 0: return False
		
	return True
	
def divisors(n):
	c = 2
	end = int(n ** .5)
	for i in range(2, end + 1):
		if n % i == 0:
			c += 2
	if end * end == n:
		c -= 1
	
	return c
	
def max_divisors(n):
	max_n = 3	
	max_div = 2
	i = t = 3
	while max_div <= n:
		t += i
		div = divisors(t)
		if div > max_div:
			max_n = t
			max_div = div
		i += 1
		
	return max_n
	
print(max_divisors(500))
