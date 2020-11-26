#-----------------------------------------------------------------------
# transpose-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

from matrix import Matrix

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


# Tests --------------------------------------------------------------

print( Matrix(list_10) )
print( Matrix(list_10).transpose() )

print( Matrix(list_11) )
print( Matrix(list_11).transpose() )

print( Matrix(list_12) )
print( Matrix(list_12).transpose() )

print( Matrix(list_12) )
print( Matrix(list_12).transpose() )