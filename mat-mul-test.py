from matrix import Matrix

# empty vector
list_10 = [[]]

# 4x1 col vector
list_11 = [[1],[2],[3],[4]]

# 1x3 row vector
list_12 = [[1,2,3]]

# 2x3 matrix  
list_21 = [[1,2,3],[4,5,6]]

# 4x3 matrix  
list_22 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 3x3 matrix  
list_23 = [[1,2,3],[4,5,6],[7,8,9]]

# 1x1 matrix
list_31 = [[1]]

# 1x1 matrix
list_32 = [[2]]

#####################
a,b,c = Matrix(list_21), Matrix(list_22), Matrix(list_23)

product = b.dot(c)

print(product)

#####################
d,e = Matrix(list_11), Matrix(list_12)

product = d.dot(e)

print(product)

#####################
# f,g = Matrix(list_31), Matrix(list_32)

# product = f.dot(g)

# print(product)
# print(list_31@list_32)