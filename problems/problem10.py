# Sieve of Eratosthenes
def sieve(n):
	l = [True for i in range(n)]
	for i in range(3, int(n ** .5) + 1, 2): # only sieving out odd numbers since there's no need to test for primality of even numbers
		if l[i]:
			for j in range(i * i, n, i):
				l[j] = False			
	return l
	
n = 2000000
primes = sieve(n)
print(sum(i for i in range(3, n, 2) if primes[i]) + 2)
