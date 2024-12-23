
def terminal_fuerza_bruta(a, d, r, i, k, x, y):
    n = len(x)
    m = len(y)

    # Función recursiva que explora todos los caminos
    def explorar(ii, jj, costo_actual, operaciones):
        # Caso base: hemos terminado ambas cadenas
        if ii == n and jj == m:
            return costo_actual, operaciones

        # Caso 1: si hemos terminado la cadena x pero no y, debemos insertar el resto de y
        if ii == n:
            operaciones += [f"Insertar {y[jj:]}"]
            return costo_actual + (m - jj) * i, operaciones

        # Caso 2: si hemos terminado la cadena y pero no x, debemos borrar el resto de x
        if jj == m:
            costo_borrar = costo_actual + (n - ii) * d
            operaciones_borrar = operaciones + [f"Borrar {x[ii:]}"]
            costo_kill = costo_actual + k
            operaciones_kill = operaciones + ["Kill"]
            return min((costo_borrar, operaciones_borrar), (costo_kill, operaciones_kill))

        # Si los caracteres actuales coinciden, seguimos avanzando (sin costo adicional)
        costo_avanzar = float('inf')
        operaciones_avanzar = operaciones
        if x[ii] == y[jj]:
            costo_avanzar, operaciones_avanzar = explorar(ii + 1, jj + 1, costo_actual + a, operaciones + [f"Avanzar {x[ii]}"])

        # Exploramos las opciones de reemplazar, borrar, insertar o aplicar kill
        costo_reemplazar, operaciones_reemplazar = explorar(ii + 1, jj + 1, costo_actual + r, operaciones + [f"Reemplazar {x[ii]} por {y[jj]}"])
        costo_borrar, operaciones_borrar = explorar(ii + 1, jj, costo_actual + d, operaciones + [f"Borrar {x[ii]}"])
        costo_insertar, operaciones_insertar = explorar(ii, jj + 1, costo_actual + i, operaciones + [f"Insertar {y[jj]}"])
        costo_kill, operaciones_kill = explorar(n, jj, costo_actual + k + (m - jj) * i, operaciones + ["Kill"])

        # Seleccionamos el costo y operaciones del camino mínimo
        costo_minimo, operaciones_minimas = min(
            (costo_avanzar, operaciones_avanzar), 
            (costo_reemplazar, operaciones_reemplazar), 
            (costo_borrar, operaciones_borrar), 
            (costo_insertar, operaciones_insertar), 
            (costo_kill, operaciones_kill)
        )

        return costo_minimo, operaciones_minimas

    # Llamamos a la función recursiva desde el inicio con costo 0 y una lista vacía de operaciones
    costo_minimo, operaciones_realizadas = explorar(0, 0, 0, [])
    
    # Mostramos el costo mínimo y las operaciones realizadas
    return costo_minimo, operaciones_realizadas

