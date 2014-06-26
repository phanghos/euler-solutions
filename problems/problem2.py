fib1, fib2 = 1, 2
s = 2 # 2 is even, we add it to the sum
fib3 = fib1 + fib2
while fib3 <= 4000000:
	if fib3 % 2 == 0:
		s += fib3
	fib1, fib2 = fib2, fib3
	fib3 = fib1 + fib2
print(s)
