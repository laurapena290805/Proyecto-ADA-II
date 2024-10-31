a = 1
d = 2
r = 3
i = 2
k = 1

def fuerza_bruta(x, y):
    n = len(x)
    m = len(y)

    def explorar(ii, jj, costo_actual):
        if ii == n and jj == m:
            return costo_actual

        if ii == n:
            return costo_actual + (m - jj) * i

        if jj == m:
            costo_borrar = costo_actual + (n - ii) * d
            costo_kill = costo_actual + k
            return min(costo_borrar, costo_kill)

        if x[ii] == y[jj]:
            costo_avanzar = explorar(ii + 1, jj + 1, costo_actual + a)
        else:
            costo_avanzar = float('inf')

        costo_reemplazar = explorar(ii + 1, jj + 1, costo_actual + r)
        costo_borrar = explorar(ii + 1, jj, costo_actual + d)
        costo_insertar = explorar(ii, jj + 1, costo_actual + i)
        costo_kill = explorar(n, jj, costo_actual + k + (m - jj) * i)
        return min(costo_avanzar, costo_reemplazar, costo_borrar, costo_insertar, costo_kill)

    # Llamamos a la función recursiva desde el inicio con costo 0 y una lista vacía de operaciones
    costo_minimo, operaciones_realizadas = explorar(0, 0, 0, [])
    
    # Mostramos el costo mínimo y las operaciones realizadas
    return costo_minimo, operaciones_realizadas

