import transpose as Transpose
import multiplication as Multiplication
import inverse as Inverse

X = [[1, 80, 2, 5], [1, 100, 3, 10], [1, 120, 4, 2], [1, 90, 3, 8], [1, 110, 3, 4]]
Y = [1300, 1500, 2000, 1400, 1800]
TX = Transpose.T(X)

TX_X = Multiplication.M(TX, X)
I_TX_X = Inverse.I1(TX_X)

I_TX_X_TX = Multiplication.M(I_TX_X, TX)
B = Multiplication.M(I_TX_X_TX, [[e] for e in Y])

print(B)
