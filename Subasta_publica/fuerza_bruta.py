def subasta_fuerza_bruta(A, B, n, ofertas):
    # Función auxiliar para calcular el valor total de una asignación
    def calcular_valor(asignacion):
        valor_total = 0
        acciones_restantes = A

        # Iteramos sobre las ofertas
        for i in range(n):
            if ofertas[i][0] >= B:  # Solo considerar ofertas que cumplen con el umbral de precio
                valor_total += asignacion[i] * ofertas[i][0]  # oferta[i][0] es el precio
                acciones_restantes -= asignacion[i]  # Restar las acciones asignadas

        # Asignar las acciones restantes a la oferta del gobierno
        valor_total += ofertas[n][0] * acciones_restantes  # oferta[n][0] es el precio del gobierno
        
        return valor_total

    # Variables para almacenar la mejor asignación y valor
    mejor_asignacion = None
    mejor_valor_total = 0

    # Función recursiva para generar combinaciones
    def combinar(i, acciones_restantes, asignacion_actual):
        nonlocal mejor_asignacion, mejor_valor_total
        if i == n:  # Si llegamos al final de las ofertas
            asignacion_actual[i] = acciones_restantes  # Asignamos las acciones restantes al gobierno
            valor_total = calcular_valor(asignacion_actual)
            if valor_total > mejor_valor_total:
                mejor_valor_total = valor_total
                mejor_asignacion = asignacion_actual[:]
            return

        # Si la oferta no cumple el umbral, saltamos a la siguiente
        if ofertas[i][0] < B:  # ofertas[i][0] es el precio de la oferta
            combinar(i + 1, acciones_restantes, asignacion_actual)
            return

        min_acciones = ofertas[i][1]  # ofertas[i][1] es el mínimo de acciones
        max_acciones = min(ofertas[i][2], acciones_restantes)  # ofertas[i][2] es el máximo de acciones
        
        # Probar todas las posibles asignaciones de acciones para la oferta actual
        for x in range(min_acciones, max_acciones + 1):
            asignacion_actual[i] = x
            combinar(i + 1, acciones_restantes - x, asignacion_actual)
        
        asignacion_actual[i] = 0  # Resetear la asignación actual
        combinar(i + 1, acciones_restantes, asignacion_actual)

    # Inicialización con un espacio extra para la oferta del gobierno
    combinar(0, A, [0] * (n + 1))

    # Si no encontramos una mejor asignación, usar la asignación inicial (que es todo 0)
    if mejor_asignacion is None:
        mejor_asignacion = [0] * (n + 1)

    # Calcular el valor total de la mejor asignación encontrada
    total = calcular_valor(mejor_asignacion)

    return mejor_asignacion, total


