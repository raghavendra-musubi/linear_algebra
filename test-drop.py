from matrix import Matrix

list_33a = [[10,60,30],[50,20,70],[40,80,90]]

print(Matrix(list_33a))
print(Matrix(list_33a).drop(1,2))

list_44 = [[1,6,3,4],[6,9,1,1],[3,0,3,2],[4,1,2,6]]

print(Matrix(list_44))
print(Matrix(list_44).drop(3,0))

