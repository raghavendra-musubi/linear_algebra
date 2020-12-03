from matrix import Matrix

## single element access tests -----------------------------------------------------------------

# list_33 = [[10,60,30],[50,20,70],[40,80,90]]
# mat_a = Matrix(list_33)
# print(mat_a[1,2])
# print(mat_a[0,1])

# s_00 = slice(0,3,2)
# print(isinstance(s_00, slice))
# print(s_00)
# print(s_00.start)
# print(s_00.stop)
# print(s_00.step)

## chunk access tests --------------------------------------------------------------------------

# init mat -----------------------------------------------------------
list_44 = [[1,6,3,4],[6,9,1,1],[3,0,3,2],[4,1,2,6]]
mat_b = Matrix(list_44)
print(mat_b)

# extract plucked matrices -------------------------------------------

# slice row and slice col access ----------------------------

# # square and rectangular chunks 
# plucked_b = mat_b[1:3,1:4]
# print(plucked_b)
# plucked_b = mat_b[1:3,1:2]
# print(plucked_b)
# plucked_b = mat_b[3:1:-1,1:3]
# print(plucked_b)
# plucked_b = mat_b[1:3,3:1:-1]
# print(plucked_b)

# index row and sliced col access --------------------
plucked_b = mat_b[2,1:3]
print(plucked_b)
plucked_b = mat_b[1,0:3]
print(plucked_b)

# slice row and index col access --------------------
# plucked_b = mat_b[1:3,1]
# print(plucked_b)

