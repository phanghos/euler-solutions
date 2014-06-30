def factorial(n):
	f = 1
	for i in range(n, 1, -1):
		f *= i
		
	return f
	
def sum_factorials(n):
	s, aux = 0, n
	while n > 0:
		div = n // 10
		s += factorial(n - div * 10)
		if s > aux:
			return s
		n = div
		
	return s
	
s = 0
end = factorial(9)
for i in range(10, end):
	if i == sum_factorials(i):
		s += i
print(s)
