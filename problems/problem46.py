def sieve(n):
	l = [True for i in range(n)]
	end = int(n ** .5)
	for i in range(3, end + 1, 2):
		if l[i]:
			for j in range(i * i, n, i):
				l[j] = False
				
	return l
	
def next_prime(n):
	p = n - 2
	while not primes[p]:
		p -= 2
		
	return p	
	
def can_be_written(n):
	p = n
	while p > 3:
		p = next_prime(p)
		s = 0
		i = 1
		while s < n:
			s = p + 2 * (i * i)
			if s == n:
				return True
			i += 1
			
	return False
	
def find():
	i = 9
	while 1:
		if not primes[i] and not can_be_written(i):
			return i
		i += 2
	
primes = sieve(50000)
print(find())
