from matrix import Matrix

# 1x1 matrix whose inverse exists ------------------------------------
list_61 = [[4]]
# inverse matrix is [[0.6, -0.7],[-0.2, 0.4]]
print(Matrix.inv(Matrix(list_61)))

# 2x2 matrix whose inverse exists ------------------------------------
list_62 = [[4, 7],[2, 6]]
# inverse matrix is [[0.6, -0.7],[-0.2, 0.4]]
print(Matrix.inv(Matrix(list_62)))

# 3x3 matrix whose inverse exists ------------------------------------
list_63 = [[3, 0, 2],[2, 0, -2],[0, 1, 1]]
# inverse matrix is [[0.2, 0.2, 0],[-0.2, 0.3, 1],[0.2, -0.3, 0]]
print(Matrix.inv(Matrix(list_63)))
