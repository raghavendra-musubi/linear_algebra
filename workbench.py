from matrix import Matrix

# a = Matrix([2,3,1,4])
# print(a)
# print(type(a))
# print(Matrix.is_numeric_list([2,3,[],4]))

list_a = [1,2,3,4]
list_b = [[1],[2],[3],[4]]
list_c = [[1],[2],[],[4]]
list_d = [2,3,[],4]
b = Matrix(list_b)
print(b)
print(type(b))
print(Matrix.is_nested_list(list_a))