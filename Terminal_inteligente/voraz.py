a = 1
d = 2
r = 3
i = 2
k = 1

def programacion_voraz(x, y):
    n = len(x)
    m = len(y)
    
    ii, jj = 0, 0
    costo_total = 0
    sol = []

    while ii < n or jj < m:
        if ii < n and jj < m and x[ii] == y[jj]:
            sol.append("Advance")
            costo_total += a
            ii += 1
            jj += 1
        
        elif ii == n:
            sol.append("Insert")
            costo_total += i
            jj += 1

        elif jj == m:
            costo_borrar = (n - ii) * d
            if k < costo_borrar:
                sol.append("Kill")
                costo_total += k
                break
            else:
                sol.append("Delete")
                costo_total += d
                ii += 1

        else:
            costo_avanzar = a if x[ii] == y[jj] else float('inf')
            costo_reemplazar = r
            costo_borrar = d
            costo_insertar = i
            costo_kill = k + (m - jj) * i

            mejor_opcion = min(costo_avanzar, costo_reemplazar, costo_borrar, costo_insertar, costo_kill)

            if mejor_opcion == costo_avanzar:
                sol.append("Advance")
                costo_total += a
                ii += 1
                jj += 1
            elif mejor_opcion == costo_reemplazar:
                sol.append("Replace")
                costo_total += r
                ii += 1
                jj += 1
            elif mejor_opcion == costo_borrar:
                sol.append("Delete")
                costo_total += d
                ii += 1
            elif mejor_opcion == costo_insertar:
                sol.append("Insert")
                costo_total += i
                jj += 1
            elif mejor_opcion == costo_kill:
                sol.append("Kill")
                costo_total += k
                break

    while jj < m:
        sol.append("Insert")
        costo_total += i
        jj += 1
    
    print(f"El costo total por programación voraz es: {costo_total}")
    print("Secuencia de operaciones:")
    print(sol)

x = "frances"
y = "francec"
programacion_voraz(x, y)

x2 = "algorithm"
y2 = "altruistic"
programacion_voraz(x2, y2,)

x3 = "francesa"
y3 = "ancestro"
programacion_voraz(x3, y3)
