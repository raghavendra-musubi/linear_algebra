#-----------------------------------------------------------------------
# transpose-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------
from matrix import Matrix

# empty list
list_o = []

# vector list
list_a = [1,2,3,4]

# matrix list
list_a = [1,2,3,4]

# 2x3 matrix for transpose 
list_f = [[1,2,3],[4,5,6]]

# 4x3 matrix for transpose 
list_g = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 3x3 matrix for transpose 
list_h = [[1,2,3],[4,5,6],[7,8,9]]

# Tests --------------------------------------------------------------

# empty matrix transpose
print(Matrix(list_o))
print(Matrix(list_o).transpose())

# vector transpose 
print(Matrix(list_a))
print(Matrix(list_a).transpose())

# matrix transpose 
print(Matrix(list_f))
print(Matrix(list_f).transpose())

print(Matrix(list_g))
print(Matrix(list_g).transpose())

print(Matrix(list_h))
print(Matrix(list_h).transpose())

