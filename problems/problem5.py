# Euclidean algorithm
def gcd(u, v):
	if v == 0:
		return u
	return gcd(v, u % v)
	
def lcm(u, v):
	return (u * v) // gcd(u, v)
	
mult = lcm(2, 3)
for i in range(4, 21):
	mult = lcm(mult, i)
print(mult)
