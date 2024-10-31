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
        #condicion para kill
        if i > 1 and x[i-1] == y[j-2] and x[i-2] == y[j-1]:
            M[i][j] = min(M[i][j], M[i-2][j-2] + k)


    i, j = n, m
    sol = []
    while ii < n or jj < m:
        # Si ambos caracteres son iguales, avanzamos
        if ii < n and jj < m and x[ii] == y[jj]:
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
                jj += 1

    # Añadimos cualquier operación pendiente
    while ii < n:
        sol.append("Delete")
        ii += 1
    while jj < m:
        sol.append("Insert")
        j -= 1

    sol.reverse()
    return sol, M[0][0]

if __name__ == '__main__':
    x = "ingenioso"
    y = "ingeniero"
    terminal_inteligente(x, y)

    x2 = "algorithm"
    y2 = "altruistic"
    terminal_inteligente(x2, y2)
