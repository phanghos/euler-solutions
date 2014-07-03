def sum_digits(n):
	s = 0
	while n > 0:
		div = n // 10
		s += n - div * 10
		n = div	
	return s
	
print(sum_digits(2 ** 1000))
