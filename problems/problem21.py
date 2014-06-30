def sum_divisors(n):
	s, d, end = 1, 2, int(n ** .5)
	while d <= end:
		if n % d == 0:
			s += d
		d += 1
	if s != 1:
		end = n // 2
		while d <= end:
			if n % d == 0:
				s += d
			d += 1
	
	return s
	
def amicable(u, v):
	return u == sum_divisors(v)

def sum_amic_under(n):
	amic = []
	s = 0
	i = 220
	while i < n:
		div_sum = sum_divisors(i)
		if amicable(i, div_sum) and i != div_sum:
			s += i
			amic.append(i)
			if not div_sum in amic:
				i = div_sum
			else:
				i += 1
		else:
			i += 1
			
	return s
	
print(sum_amic_under(10000))
