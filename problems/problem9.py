def solution(a, b, c):
	return a * a + b * b == c * c

"""
for i in range(1000):
	for j in range(i + 1, 1000):
		for k in range(j + 1, 1000):
			if solution(i, j, k) and i + j + k == 1000:
				print(i, j, k)
"""
m = 5
while 1:
	a = 2 * m
	b = m * m - 1
	c = m * m + 1
	if solution(a, b, c) and a + b + c == 1000:
		print(a, b, c, "=", a * b * c)
		break
	m += 1
