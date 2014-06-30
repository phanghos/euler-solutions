# Sieve of Eratosthenes
def sieve(n):
	l = [True for i in range(n)]
	end = int(n ** .5)
	for i in range(2, end + 1):
		if l[i]:
			for j in range(i * i, n, i):
				l[j] = False
				
	return l
	
def digits(n):
	c = 0
	while n > 0:
		c += 1
		n //= 10
		
	return c

# to rotate number, we computer factor = 10^(#digits - 1)
# we substract first_digit * factor from n
# we multiply that by 10 and add the original first digit
# example: 123
# #digits = 3
# factor = 10^(3 - 1) = 100
# 123 - 100 = 23
# 23 * 10 = 230
# 230 + 1 = 231
# rotation done
def rotate(n, f):
	d = n // f
	n -= d * f
	n = n * 10 + d
	
	return n

def circular_prime(n):
	d = digits(n)
	f = 10 ** (d - 1)
	for i in range(d):
		n = rotate(n, f)
		if not primes[n]:
			return False
		
	return True
	
def count_circular_primes(n):
	c = 1
	for i in range(3, n, 2):
		if primes[i] and circular_prime(i):
			c += 1
			
	return c
		
primes = sieve(1000000)
print(count_circular_primes(1000000))
