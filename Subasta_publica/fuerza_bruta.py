def subasta_fuerza_bruta(A, B, n, ofertas):
    # Crear listas de precios, mínimos y máximos para cada oferta (incluyendo la oferta del gobierno)
    precios = [oferta[0] for oferta in ofertas]
    minimos = [oferta[1] for oferta in ofertas]
    maximos = [oferta[2] for oferta in ofertas]
    
    # Variable para almacenar el mejor valor total y la mejor asignación
    mejor_valor = 0
    mejor_asignacion = [0] * (n + 1)  # Incluyendo la oferta del gobierno

    # Función recursiva para probar todas las combinaciones posibles
    def probar_combinacion(i, acciones_restantes, valor_actual, asignacion_actual):
        nonlocal mejor_valor, mejor_asignacion

        # Si hemos considerado todas las ofertas (menos la del gobierno)
        if i == n:
            # Asignar todas las acciones restantes a la oferta del gobierno
            asignacion_actual[-1] = acciones_restantes
            valor_actual += acciones_restantes * precios[-1]  # Precio de la oferta del gobierno
            
            # Actualizamos el mejor valor si el valor actual es mayor
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_asignacion = asignacion_actual[:]
            return

        # Caso en que no se asignan acciones a la oferta actual
        probar_combinacion(i + 1, acciones_restantes, valor_actual, asignacion_actual)

        # Caso en que se asignan acciones a la oferta actual (de minimos[i] a maximos[i])
        for x in range(minimos[i], min(maximos[i], acciones_restantes) + 1):
            asignacion_actual[i] = x
            nuevo_valor = valor_actual + x * precios[i]
            probar_combinacion(i + 1, acciones_restantes - x, nuevo_valor, asignacion_actual)
            asignacion_actual[i] = 0  # Deshacer la asignación después de probar

    # Llamada inicial a la función recursiva
    probar_combinacion(0, A, 0, [0] * (n + 1))

    return mejor_asignacion, mejor_valor
