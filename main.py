from matrix import Matrix

test = Matrix(4, 3)
test_2 = Matrix(3, 5)

result = test.__mul__(test_2)
print(result.__str__())
