def sieve(n):
	end = int(n ** .5)
	l = [True for i in range(n + 1)]
	l[0] = l[1] = False
	for i in range(2, end + 1):
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
