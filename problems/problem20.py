def factorial(n):
	f = 1
	for i in range(n, 1, -1):
		f *= i	
	return f
	
def sum_digits(n):
	s = 0
	while n > 0:
		div = n // 10
		s += n - div * 10
		n = div
	return s
	
print(sum_digits(factorial(100)))
