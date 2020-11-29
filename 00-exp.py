from matrix import Matrix

list_33 = [[1,6,3,4],[6,1,1,1],[3,1,3,2],[4,1,2,6]]

print(list_33[0][1])
print(list_33[:][1])

mat_a = Matrix(list_33)
mat_a[0][1]