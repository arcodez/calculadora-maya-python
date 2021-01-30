import numpy as np

# Cajas de Simbolos
def crear_cajas():# Esto es un arreglo
    v = np.array(["Algo", 2, 3, 4, 5])

    # Esto es una matriz
    matriz = np.array([[1, 2, 3],    [2, 3, 4]])

    # Caja donde se guardan los puntos con mas valor de forma larga
    downbox = np.zeros((4,4))

    # Caja donde se guardan los puntos , rayas y conchas
    upbox = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ["", "=", "=", "="]])

    print("=============== Ejemplos =================")
    print(v)
    print(matriz)

    print("=============== Simbologia Maya =================")

    print(downbox)
    print("=============== Separacion de cajas =================")
    print(upbox)

crear_cajas()