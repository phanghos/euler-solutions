def sieve(n):
	l = [True for i in range(n + 1)]
	l[0] = l[1] = False
	end = int(n ** .5)
	for i in range(2, end + 1):
		if l[i]:
			for j in range(i * i, n + 1, i):
				l[j] = False
				
	return l
	
def factor(n):
	f = 1
	while f <= n:
		f *= 10
		
	return f // 10
	
def remove_from_left(n, f):
	d = n // f
	
	return n - d * f
	
def remove_from_right(n):
	return n // 10

def truncatable(n):
	aux = n
	f = factor(n)
	while f > 1:
		n = remove_from_left(n, f)
		aux = remove_from_right(aux)
		if not primes[n] or not primes[aux]:
			return False
		f //= 10
		
	return True
	
def find_truncatable():
	c, s, i = 0, 0, 11
	while c < 11:
		if primes[i] and truncatable(i):
			c += 1
			s += i
		i += 2
		
	return s

primes = sieve(1000000)
print(find_truncatable())
