squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Omit the temporary variable for more concise
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)