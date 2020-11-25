#-----------------------------------------------------------------------
# dot-product-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

from matrix import Matrix

# vector * vector 

a = Matrix([1,2,3])
b = Matrix([3,4,5])

c = a.dot(b)
print(c)

# matrix * vector 

a = Matrix([[1,2],[3,4]])
b = Matrix([3,4])

c = a.dot(b)
print(c)

# vector * matrix 

a = Matrix([3,4])
b = Matrix([[1,2],[3,4]])

c = a.dot(b)
print(c)

# matrix * matrix





