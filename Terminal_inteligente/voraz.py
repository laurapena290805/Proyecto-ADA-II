
def terminal_inteligente_voraz(a, d, r, i, k, x, y):
    n = len(x)
    m = len(y)
    
    ii, jj = 0, 0
    costo_total = 0
    sol = []

    while ii < n or jj < m:
        if ii < n and jj < m and x[ii] == y[jj]:
            sol.append("Advance " + x[ii])
            costo_total += a
            ii += 1
            jj += 1
        
        elif ii == n:
            sol.append("Insert " + y[jj])
            costo_total += i
            jj += 1

        elif jj == m:
            costo_borrar = (n - ii) * d
            if k < costo_borrar:
                sol.append("Kill")
                costo_total += k
                break
            else:
                sol.append("Delete " + x[ii])
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
                sol.append("Advance " + x[ii])
                costo_total += a
                ii += 1
                jj += 1
            elif mejor_opcion == costo_reemplazar:
                sol.append("Replace " + x[ii] + " por " + y[jj])
                costo_total += r
                ii += 1
                jj += 1
            elif mejor_opcion == costo_borrar:
                sol.append("Delete " + x[ii])
                costo_total += d
                ii += 1
            elif mejor_opcion == costo_insertar:
                sol.append("Insert " + y[jj])
                costo_total += i
                jj += 1
            elif mejor_opcion == costo_kill:
                sol.append("Kill")
                costo_total += k
                break

    while jj < m:
        sol.append("Insert " + y[jj])
        costo_total += i
        jj += 1
    
    return costo_total, sol

