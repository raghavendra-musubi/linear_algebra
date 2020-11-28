# Imports --------------------------------------------------------------

from matrix import Matrix

# Define Inputs --------------------------------------------------------

## 00. invalid inputs -------------------------------

# invalid list
list_00 = []

# vector list
list_01 = [1,2,3,4]

# a non-entirely-numerical list
list_02 = [2,3,[],4]

# invalid list input
list_03 = [[1],[2],[],[4]]

# a non-rectangular list
list_04 = [[1,2],[3,4],[5],[6,7,8]]


## 01. valid inputs ---------------------------------

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

## Size Tests --------------------------------------

print(Matrix.get_size(list_10))
print(Matrix.get_size(list_11))
print(Matrix.get_size(list_12))
print(Matrix.get_size(list_21))
print(Matrix.get_size(list_22))
print(Matrix.get_size(list_23))

## Multi Test --------------------------------------

print(Matrix.dim_check_for_mult(Matrix(list_11),Matrix(list_12) ))
print(Matrix.dim_check_for_mult(Matrix(list_22),Matrix(list_23) ))

print(Matrix.dim_check_for_mult(Matrix(list_23),Matrix(list_22) ))
