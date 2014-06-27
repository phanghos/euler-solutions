def prime(n):
	if n == 2: return True
	if n % 2 == 0 or n == 1: return False
	end = int(n ** .5)
	for i in range(3, end + 1, 2):
		if n % i == 0: return False
	
	return True

def nthprime(n):
	c = 1
	nth = 3
	while c < n:
		if prime(nth):
			c += 1
		nth += 2
	
	return nth - 2

print(nthprime(10001))
