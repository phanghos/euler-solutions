def digits(n):
	c = 0
	while n > 0:
		c += 1
		n //= 10
		
	return c
	
fib1 = fib2 = 1
fib3 = fib1 + fib2
c = 3
while digits(fib3) != 1000:
	fib1, fib2 = fib2, fib3
	fib3 = fib1 + fib2
	c += 1
print(c)
