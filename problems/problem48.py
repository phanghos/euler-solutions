def sum_series(n):
	s = 0
	for i in range(1, n + 1):
		s += i ** i
		
	return s
	
def digits(n, d):
	num_str = ""
	for i in range(d):
		div = n // 10
		num_str = str(n - div * 10) + num_str
		n = div
		
	return int(num_str)
	
print(digits(sum_series(1000), 10))
