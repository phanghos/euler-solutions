palindrome = lambda string: string == string[::-1]
print(max(i * j for i in range(100, 1000) for j in range(i, 1000) if palindrome(str(i * j))))
