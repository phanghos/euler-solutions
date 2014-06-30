import timeit

# Sieve of Eratosthenes
def sieve(n):
	l = [True for i in range(n)]
	end = int(n ** .5)
	for i in range(3, end + 1, 2): # only sieving out odd numbers since there's no need to test for primality of even numbers
		if l[i]:
			for j in range(i * i, n, i):
				l[j] = False
				
	return l
	
def sum_primes(n):
	primes = sieve(n)
	s = 2
	for i in range(3, n, 2):
		if primes[i]:
			s += i
			
	return s
	
print(sum_primes(2000000))
