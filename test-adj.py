from matrix import Matrix

# 1x1 matrix whose determinant is (-4) -------------------------------
list_51 = [[-4]]
mat_51 = Matrix(list_51)
print(Matrix.det(mat_51))

# 2x2 matrix whose determinant is (10) -------------------------------
list_52 = [[4,1],[2,3]]
mat_52 = Matrix(list_52)
print(Matrix.det(mat_52))

# 3x3 matrix whose determinant is (-6) -------------------------------
list_53 = [[-2,3,-1],[5,-1,4],[4,-8,2]]
mat_53 = Matrix(list_53)
print(Matrix.det(mat_53))

# 4x4 matrix whose determinant is (-279) -----------------------------
list_54 = [[7,4,2,0],[6,3,-1,2],[4,6,2,5],[8,2,-7,1]]
mat_54 = Matrix(list_54)
print(Matrix.det(mat_54))