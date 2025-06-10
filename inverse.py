import numpy as np
from typing import List


def I1(matriz_lista: List[List[float]]) -> np.ndarray | None:
    """
    Calcula la inversa de una matriz usando NumPy, validando su determinante.

    Args:
        matriz_lista: La matriz de entrada como una lista de listas de números.

    Returns:
        Un array de NumPy representando la matriz inversa si existe, o None si no.
    """
    # 1. Convertir la lista de listas a un array de NumPy
    matriz_np = np.array(matriz_lista)

    # 2. Validar que sea una matriz cuadrada
    # np.shape devuelve una tupla (filas, columnas)
    if matriz_np.shape[0] != matriz_np.shape[1]:
        print("❌ Error: La matriz no es cuadrada y no puede tener inversa.")
        return None

    # 3. Calcular el determinante
    determinante = np.linalg.det(matriz_np)
    # print(f"Determinante de la matriz: {determinante}")

    # 4. Validar que el determinante no sea cero (o muy cercano a cero)
    # Se usa una tolerancia para números de punto flotante
    if abs(determinante) < 1e-9:  # 1e-9 es 0.000000001, una tolerancia común
        print(
            "❌ Error: El determinante es cero (o muy cercano a cero). La matriz no tiene inversa."
        )
        return None

    # 5. Calcular la inversa
    inversa_np = np.linalg.inv(matriz_np)
    return inversa_np.tolist()
