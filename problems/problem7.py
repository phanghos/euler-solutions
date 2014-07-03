def prime(n):
	if n == 2:
		return True
	if n % 2 == 0 or n == 1:
		return False
	for i in range(3, int(n ** .5) + 1, 2):
		if n % i == 0:
			return False
	return True

def nthprime(n):
	c, nth = 1, 3
	while c < n:
		if prime(nth):
			c += 1
		nth += 2
	return nth - 2

print(nthprime(10001))
