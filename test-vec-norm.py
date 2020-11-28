# Imports --------------------------------------------------------------

from matrix import Matrix

# Define Inputs --------------------------------------------------------

list_11 = [[1],[2],[3],[4]]
list_12 = [[1,2,3]]

# compute default norm (2-norm)
print( Matrix(list_11).vec_norm() )
print( Matrix(list_12).vec_norm() )

# compute 1-norm
print( Matrix(list_11).vec_norm(1) )
print( Matrix(list_12).vec_norm(1) )

# compute 3-norm
print( Matrix(list_11).vec_norm(3) )
print( Matrix(list_12).vec_norm(3) )