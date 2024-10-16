import numpy as np

def subasta_voraz(A, B, n, ofertas):
    ofertas_validas = [(i, oferta) for i, oferta in enumerate(ofertas) if oferta[0] >= B]
    ofertas_validas.sort(key=lambda x: x[1][0], reverse=True)  

    asignacion_optima = np.zeros(n + 1, dtype=int) 
    valor_total = 0
    acciones_restantes = A  
    for indice, oferta in ofertas_validas:
        precio, minimo, maximo = oferta  

        if acciones_restantes <= 0:
            break

       
        cantidad_asignar = min(maximo, acciones_restantes)
      

        if cantidad_asignar < minimo:
            continue

        asignacion_optima[indice] = cantidad_asignar
        valor_total += cantidad_asignar * precio
        acciones_restantes -= cantidad_asignar

    return asignacion_optima, valor_total

