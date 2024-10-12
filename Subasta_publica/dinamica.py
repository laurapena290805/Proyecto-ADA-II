"""
Proyecto 1: Programacion dinamica y voraz
Analisis de algoritmos II

EL PROBLEMA DE LA SUBASTA

Laura Tatiana Coicue
Laura Sofia Peñaloza
Santiago Reyes Rodriguez
"""
"""
"""

import numpy as np

def subasta_dp(A, B, n, ofertas):
    
    precios = np.array([oferta[0] for oferta in ofertas])
    minimos = np.array([oferta[1] for oferta in ofertas])
    maximos = np.array([oferta[2] for oferta in ofertas])


    dp = np.zeros((n + 1, A + 1))

    # Rellenar la matriz de programación dinámica
    for i in range(n):
        dp[i + 1] = dp[i].copy()  # Copiar la fila anterior

        # Solo considerar precios que sean mayores o iguales al umbral
        if precios[i] >= B:
            for x in range(minimos[i], min(maximos[i], A) + 1):
                dp[i + 1, x:] = np.maximum(dp[i + 1, x:], dp[i, :-x] + x * precios[i])

    # Recuperar la asignación óptima
    acciones_restantes = A
    mejor_asignacion = np.zeros(n + 1, dtype=int)

    for i in range(n - 1, -1, -1):
        if precios[i] < B:
            continue
        for x in range(minimos[i], min(maximos[i], acciones_restantes) + 1):
            if acciones_restantes >= x and dp[i + 1][acciones_restantes] == dp[i][acciones_restantes - x] + x * precios[i]:
                mejor_asignacion[i] = x
                acciones_restantes -= x
                break

    # Si quedan acciones sin asignar, se asignan a la última oferta
    if acciones_restantes > 0:
        mejor_asignacion[n] = acciones_restantes

   
    valor_final = int(dp[n][A] + (ofertas[n][0] * mejor_asignacion[n]))
    return valor_final, mejor_asignacion.tolist()


