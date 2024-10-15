def subasta_voraz(A, B, n, ofertas):
    precios = [oferta[0] for oferta in ofertas]
    minimos = [oferta[1] for oferta in ofertas]
    maximos = [oferta[2] for oferta in ofertas]

    mejor_asignacion = [0] * n

    ofertas_ordenadas = sorted([(i, precios[i], minimos[i], maximos[i]) for i in range(n) if precios[i] >= B], key=lambda x: -x[1])

    acciones_restantes = A
    valor_total = 0

    for oferta in ofertas_ordenadas:
        idx, precio, minimo, maximo = oferta

        if acciones_restantes >= minimo:  
            asignar = min(maximo, acciones_restantes)

            if asignar >= minimo:
                mejor_asignacion[idx] = asignar
                valor_total += asignar * precio
                acciones_restantes -= asignar

        if acciones_restantes <= 0:
            break

    return valor_total, mejor_asignacion
