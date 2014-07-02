sum_squares = lambda n: n * (n + 1) * (2 * n + 1) // 6
square_sum = lambda n: ((n * (n + 1)) // 2) ** 2
print(square_sum(100) - sum_squares(100))
