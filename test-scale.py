# Imports --------------------------------------------------------------

from matrix import Matrix

# Init Values ----------------------------------------------------------

# Test scaling 

scalar_a = 0
scalar_b = 1
scalar_c = 2
scalar_d = 10

# 4x3 matrix  
list_22 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# Run Tests ----------------------------------------------------------

print(Matrix(list_22))
print(Matrix(list_22).scale(scalar_a))

print(Matrix(list_22))
print(Matrix(list_22).scale(scalar_b))

print(Matrix(list_22))
print(Matrix(list_22).scale(scalar_c))

print(Matrix(list_22))
print(Matrix(list_22).scale(scalar_d))

