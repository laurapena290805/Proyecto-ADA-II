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

a = 1
d = 2
r = 3
i = 2
k = 1

def condicion_kill(x, y, i, j):
    restantes_x = len(x) - i
    restantes_y = len(y) - j
    if restantes_x > 0:
        costo_insert_restantes = restantes_y * i
        costo_kill = k + costo_insert_restantes
        costo_replace_restantes = min(restantes_x, restantes_y) * r
        return costo_kill < costo_replace_restantes
    return False

def terminal_inteligente(x, y):
    n = len(x)
    m = len(y)
    M = np.zeros((n+1, m+1), dtype=int)

    for i in range(n + 1):
        M[i][0] = i * k
    for j in range(m + 1):
        M[0][j] = j * i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i-1][j-1] + a
            else:
                M[i][j] = min(
                    M[i-1][j-1] + r,
                    M[i-1][j] + d,
                    M[i][j-1] + i
                )

            if condicion_kill(x, y, i, j):
                M[i][j] = min(M[i][j], M[i-1][j] + k + (m - j) * i)

    print("Matriz de costos:")
    print(M)
    print("El costo mínimo es: ", M[n][m])

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
            elif M[i][j] == M[i][j-1] + i:
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
    print("Secuencia de operaciones:")
    print(sol)

x = "ingenioso"
y = "ingeniero"
terminal_inteligente(x, y)

x2 = "algorithm"
y2 = "altruistic"
terminal_inteligente(x2, y2)
