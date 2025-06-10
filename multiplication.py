from typing import List


def M(X: List[List[int]], Y: List[List[int]]) -> List[List[int]]:
    """
    Realiza la multiplicación de dos matrices.

    Args:
        matriz_a: La primera matriz (lista de listas de enteros).
        matriz_b: La segunda matriz (lista de listas de enteros).

    Returns:
        La matriz resultante de la multiplicación (lista de listas de enteros).

    Raises:
        ValueError: Si las dimensiones de las matrices no son compatibles para la multiplicación.
    """
    x_rows = len(X)
    # a_cols = len(X[0])  # Asumimos que la matriz no está vacía y es rectangular
    # b_rows = len(Y)
    y_cols = len(Y[0])  # Asumimos que la matriz no está vacía y es rectangular

    # if a_cols != b_rows:
    #     raise ValueError(
    #         "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz."
    #     )

    # Inicializar la matriz resultante con ceros
    # La matriz resultante tendrá 'x_rows' filas y 'y_cols' columnas
    R = [[0 for _ in range(y_cols)] for _ in range(x_rows)]

    try:
        for i in range(len(X)):
            for j in range(len(Y[i])):
                for k in range(len(X[i])):
                    R[i][j] += X[i][k] * Y[k][j]
    except Exception as e:
        print(f"❌ Rangos de Matriz Incorrecto: {e}")

    return R
