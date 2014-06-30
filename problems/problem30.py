def sum_powers(n, p):
	s, aux = 0, n
	while n > 0:
		div = n // 10
		s += (n - div * 10) ** p
		#if s > aux:
			#return s
		n = div
		
	return s

s = 0
for i in range(2, 5 * 9 ** 5):
	if sum_powers(i, 5) == i:
		s += i
print(s)
