def subasta_voraz(A, B, n, ofertas):
    precios = [oferta[0] for oferta in ofertas]
    minimos = [oferta[1] for oferta in ofertas]
    maximos = [oferta[2] for oferta in ofertas]

    mejor_asignacion = [0] * n

    # Filtrar y ordenar las ofertas válidas (con precios >= B) por precio de mayor a menor
    ofertas_validas = [(i, precios[i], minimos[i], maximos[i]) for i in range(n - 1) if precios[i] >= B]
    ofertas_ordenadas = sorted(ofertas_validas, key=lambda x: -x[1])

    acciones_restantes = A
    valor_total = 0

    # Asignar acciones a las ofertas ordenadas
    for idx, precio, minimo, maximo in ofertas_ordenadas:
        # Condición 1: Si ya no quedan acciones por asignar, detener el proceso
        if acciones_restantes <= 0:
            break

    return valor_total, mejor_asignacion