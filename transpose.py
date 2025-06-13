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
        AUX = []
        for row in X:
            AUX.append(row[i])
        X_A.append(AUX)

    return X_A
