def sum_digits(n):
	s = 0
	while n > 0:
		div = n // 10
		s += n - div*10
		n = div
		
	return s
	
print(max(sum_digits(i ** j) for i in range(1, 100) for j in range(1, 100)))
