"""
Proyecto 1: Programacion dinamica y voraz
Analisis de algoritmos II

EL PROBLEMA DE LA SUBASTA

Laura Tatiana Coicue
Laura Sofia Peñaloza
Santiago Reyes Rodriguez
"""
"""
    Calcula el valor óptimo de asignación de acciones para maximizar el beneficio del gobierno.
    
    Parámetros:
    - A: número total de acciones a subastar.
    - B: precio mínimo que el gobierno ofrece por las acciones sobrantes.
    - ofertas: lista de tuplas (p_i, m_i, M_i), donde:
        - p_i: precio que el oferente i está dispuesto a pagar por acción.
        - m_i: número mínimo de acciones que el oferente i está dispuesto a comprar.
        - M_i: número máximo de acciones que el oferente i está dispuesto a comprar.
    
    Retorna:
    - Las asginaciones realizadas y el valor máximo posible para la asignación de las acciones 
    """

def subasta_optima(A, B, n, ofertas):
    #arreglo para almacenar el valor máximo
    dp = [0] * (A + 1)
    # arreglo para almacenar las asignaciones
    asignacion = [[0] * n for _ in range(A + 1)]

    # Iterar sobre cada oferta
    for i in range(n):
        p_i, m_i, M_i = ofertas[i]
        # Iterar sobre la cantidad de acciones disponibles
        for a in range(A, m_i - 1, -1):
            # Evaluar cada posible asignación dentro del rango permitido
            for x in range(m_i, min(M_i, a) + 1):
                if dp[a] < dp[a - x] + p_i * x:
                    dp[a] = dp[a - x] + p_i * x
                    asignacion[a] = asignacion[a - x][:]
                    asignacion[a][i] += x

    #acciones asignadas al gobierno
    acciones_gobierno = A - sum(asignacion[A])
    
    #agregar la asignación del gobierno al resultado final
    if acciones_gobierno > 0:
        asignacion[A].append(acciones_gobierno)
    
    return asignacion[A], dp[A]
