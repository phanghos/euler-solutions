s = {}
s = {i ** j for i in range(2, 101) for j in range(2, 101) if not (i ** j) in s}
print(len(s))
