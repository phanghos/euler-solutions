def sum_digits(n):
	s = 0
	while n > 0:
		div = n // 10
		s += n - div * 10
		n = div
		
	return s

def max_sum(n):
	max_s = 0
	for i in range(1, 100):
		for j in range(1, 100):
			s = sum_digits(i ** j)
			if s > max_s:
				max_s = s
				
	return max_s
	
print(max_sum(100))
