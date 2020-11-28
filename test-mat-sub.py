from matrix import Matrix

# 4x1 col vector
list_11 = [[1],[2],[3],[4]]
list_12 = [[5],[6],[7],[8]]

print(Matrix(list_12) - Matrix(list_11))

# 2x3 matrix  
list_21 = [[1,2,3],[4,5,6]]
list_22 = [[7,8,9],[10,11,12]]

print(Matrix(list_22) - Matrix(list_21))