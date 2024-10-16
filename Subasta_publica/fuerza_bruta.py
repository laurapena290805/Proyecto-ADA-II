def subasta_fuerza_bruta(A, B, n, ofertas):
    precios = [oferta[0] for oferta in ofertas]
    minimos = [oferta[1] for oferta in ofertas]
    maximos = [oferta[2] for oferta in ofertas]

    mejor_valor = 0
    mejor_asignacion = [0] * n

    def probar_combinacion(i, acciones_restantes, valor_actual, asignacion_actual):
        nonlocal mejor_valor, mejor_asignacion

        if i == n or acciones_restantes == 0:
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_asignacion = asignacion_actual[:]
            return
        probar_combinacion(i + 1, acciones_restantes, valor_actual, asignacion_actual)

        for x in range(minimos[i], min(maximos[i], acciones_restantes) + 1):
            asignacion_actual[i] = x
            nuevo_valor = valor_actual + x * precios[i]
            probar_combinacion(i + 1, acciones_restantes - x, nuevo_valor, asignacion_actual)
            asignacion_actual[i] = 0  # Deshacer la asignación

    probar_combinacion(0, A, 0, [0] * n)

    return mejor_valor, mejor_asignacion

