import transpose as Transpose


X = [[1, 80, 2, 5], [1, 100, 3, 10], [1, 120, 4, 2], [1, 90, 3, 8], [1, 110, 3, 4]]
Y = [1300, 1500, 2000, 1400, 1800]
T_X = Transpose.T(X)

B = X * Y

print(B)
