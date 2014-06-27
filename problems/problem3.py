# largest prime factor must be <= sqrt(n)
# n is a sqrt(n)-smooth number (not a sqrt(n)-rough number)
# http://mathworld.wolfram.com/GreatestPrimeFactor.html

# Sieve of Eratosthenes
def sieve(n):
	end = int(n ** .5)
	l = [True for i in range(n + 1)]
	for i in range(3, end + 1, 2): # only sieving out odd numbers since there's no need to test for primality of even numbers
		if l[i]:
			for j in range(i * i, n + 1, i):
				l[j] = False
	
	return l
	
def largest_factor(n):
	end = int(n ** .5)
	l = sieve(end)
	for i in range(3, end + 1, 2):
		if l[i] and n % i == 0:
			p = i
	
	return p
	
n = 600851475143
print(largest_factor(n))
