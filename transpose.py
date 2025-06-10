from typing import List


def T(X: List[List[int]]) -> List[List[int]]:
    """
    Transpose of a matrix.

    Parameters
    ----------
    X : list of lists
        The matrix to be transposed.

    Returns
    -------
    list of lists
        The transposed matrix.
    """
    # return [list(row) for row in zip(*X)]
    X_A: List[List[int]] = []
    for i in range(len(X)):
        for j in range(len(X[i])):
            if len(X_A) < j + 1:
                X_A.append([])
            X_A[j].append(X[i][j])

    return X_A
