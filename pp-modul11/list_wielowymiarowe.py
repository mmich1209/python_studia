# print([1,2], [3,4])

row = [1, 2]

matrix = [row[:], row[:]]
print(matrix)

matrix[0][0] = 99
print(matrix)

