fib1, fib2 = 1, 2
s = 0
while fib2 <= 4000000:
	if fib2 % 2 == 0:
		s += fib2
	fib1, fib2 = fib2, fib1 + fib2
print(s)
