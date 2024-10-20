"""
Proyecto 1: Programacion dinamica y voraz
Analisis de algoritmos II

Laura Tatiana Coicue
Laura Sofia Peñaloza
Santiago Reyes Rodriguez
"""

#Problema de "La Terminal Inteligente"
#
#Operaciones:       Costo:
#advance            a
#replace            r
#delete             d
#insert             i
#kill               k

### ESTRATEGIA DE PROGRAMACIÓN DINAMICA
import numpy as np

def terminal_dinamica(a,d,r,ins,k,x, y):
    n = len(x)
    m = len(y)
    M = np.zeros((n+1, m+1), dtype=int)

    # Inicialización de la primera fila y columna
    for i in range(n + 1):
        M[i][0] = i * d  # Costo de eliminar todos los caracteres
    for j in range(m + 1):
        M[0][j] = j * ins  # Costo de insertar todos los caracteres

    # Llenado de la matriz M con los costos
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i-1][j-1] + a  # Avance sin costo
            else:
                M[i][j] = min(
                    M[i-1][j-1] + r,   # Reemplazo
                    M[i-1][j] + d,     # Eliminación
                    M[i][j-1] + ins    # Inserción
                )
        # Condición para Kill (intercambio de dos caracteres consecutivos)
        if i > 1 and x[i-1] == y[j-2] and x[i-2] == y[j-1]:
            M[i][j] = min(M[i][j], M[i-2][j-2] + k)

    # Trazado del camino de las operaciones
    i, j = n, m
    sol = []
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            sol.append("Advance")
            i -= 1
            j -= 1
        else:
            if M[i][j] == M[i-1][j-1] + r:
                sol.append("Replace")
                i -= 1
                j -= 1
            elif M[i][j] == M[i-1][j] + d:
                sol.append("Delete")
                i -= 1
            elif M[i][j] == M[i][j-1] + ins:
                sol.append("Insert")
                j -= 1
            else:
                sol.append("Kill")
                i -= 1
                while j > 0:
                    sol.append("Insert")
                    j -= 1

    while i > 0:
        sol.append("Delete")
        i -= 1
    while j > 0:
        sol.append("Insert")
        j -= 1

    sol.reverse()
    val = M[n][m].item() # Costo final
    return val, sol # Devuelve el costo final desde M[n][m]

