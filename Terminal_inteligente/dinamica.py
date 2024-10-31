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


def terminal_inteligente_dp(a, d, r, i, k,x, y):
    n = len(x)
    m = len(y)

    M = np.zeros((n+1, m+1))
    M.fill(np.inf)

    M[n][m] = 0

    for ii in range(n, -1, -1):
        for jj in range(m, -1, -1):
            if ii == n and jj == m:
                continue

            if ii == n:
                M[ii][jj] = (m - jj) * i
                continue

            if jj == m:
                costo_borrar = (n - ii) * d
                costo_kill = k
                if costo_kill < costo_borrar:
                    M[ii][jj] = costo_kill
                else:
                    M[ii][jj] = costo_borrar
                continue

            if x[ii] == y[jj]:
                if M[ii + 1][jj + 1] + a < M[ii][jj]:
                    M[ii][jj] = M[ii + 1][jj + 1] + a

            if M[ii + 1][jj + 1] + r < M[ii][jj]:
                M[ii][jj] = M[ii + 1][jj + 1] + r

            if M[ii + 1][jj] + d < M[ii][jj]:
                M[ii][jj] = M[ii + 1][jj] + d

            if M[ii][jj + 1] + i < M[ii][jj]:
                M[ii][jj] = M[ii][jj + 1] + i


            costo_kill = k + (m - jj) * i
            if costo_kill < M[ii][jj]:
                M[ii][jj] = costo_kill

            M[ii][jj] = min(
                M[ii][jj],
                M[ii + 1][jj + 1] + r,
                M[ii + 1][jj] + d,
                M[ii][jj + 1] + i,
                M[ii + 1][jj] + k + (m - jj) * i
            )

    ii, jj = 0, 0

    sol = []
    while ii < n or jj < m:
        # Si ambos caracteres son iguales, avanzamos
        if ii < n and jj < m and x[ii] == y[jj]:
            sol.append("Advance")
            ii += 1
            jj += 1
        # Si la operación corresponde a reemplazar un carácter
        elif ii < n and jj < m and M[ii][jj] == M[ii + 1][jj + 1] + r:
            sol.append("Replace")
            ii += 1
            jj += 1
        # Si la operación corresponde a borrar un carácter
        elif ii < n and M[ii][jj] == M[ii + 1][jj] + d:
            sol.append("Delete")
            ii += 1
        # Si la operación corresponde a insertar un carácter
        elif jj < m and M[ii][jj] == M[ii][jj + 1] + i:
            sol.append("Insert")
            jj += 1
        # Si la operación corresponde a "kill" (matar el resto del texto en 'x')
        elif ii < n and M[ii][jj] == k + (m - jj) * i:
            sol.append("Kill")
            ii = n
            while jj < m:
                sol.append("Insert")
                jj += 1

    # Añadimos cualquier operación pendiente
    while ii < n:
        sol.append("Delete")
        ii += 1
    while jj < m:
        sol.append("Insert")
        jj += 1

    return int(M[0][0]), sol
