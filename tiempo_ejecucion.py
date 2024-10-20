import time
import numpy as np
import matplotlib.pyplot as plt
import math

from Terminal_inteligente.dinamica import terminal_inteligente
from Terminal_inteligente.fuerza_bruta import fuerza_bruta
from Terminal_inteligente.voraz import programacion_voraz
from Subasta_publica.dinamica import subasta_dp
from Subasta_publica.voraz import subasta_voraz
from Subasta_publica.fuerza_bruta import subasta_fuerza_bruta

def tiempo_ejecucion(funcion, args, num_iteraciones=500):
    array = np.zeros(num_iteraciones)
    for i in range(num_iteraciones):
        inicio = time.time()
        funcion(*args)
        fin = time.time()
        array[i] = fin - inicio
    return np.mean(array)

def graficar (tiempos, nombre_grafica):
    plt.figure(figsize = (10, 5))
    plt.title("Tiempo de ejecución - " + nombre_grafica)
    plt.plot(tiempos[0], label="Programación dinámica")
    plt.plot(tiempos[1], label="Fuerza bruta")
    plt.plot(tiempos[2], label="Programación voraz")
    plt.legend()
    plt.yscale("log")
    plt.savefig('./graficas/' + nombre_grafica.replace(' ', '_').lower() + ".png")

def guardar_archivos(lista, nombres_archivos, ruta="./tiempos/"):
    
    for i in range(len(lista)):
        tiempo = lista[i]
        archivo = nombres_archivos[i].lower() + ".txt"
        with open(ruta + archivo, "w") as f:
            for t in tiempo:
                f.write(f"{t}\n")



def tiempos_terminal_inteligente():
    casos = [
        ("Ay", "Ya"),
        ("Pal", "Pup"),
        ("Mora", "More"),
        ("Aguas", "Vacas"),
        ("Destino", "Caminos"),
    ]

    costos_teoricos = [[], [], []]
    tiempos = [[], [], []]

    for caso in casos:
        result_dinamica = tiempo_ejecucion(terminal_inteligente, caso)
        result_fuerza_bruta = tiempo_ejecucion(fuerza_bruta, caso)
        result_voraz = tiempo_ejecucion(programacion_voraz, caso)

        tiempos[0].append(result_dinamica)
        tiempos[1].append(result_fuerza_bruta)
        tiempos[2].append(result_voraz)
                          
        m, n = len(caso[0]), len(caso[1])
        costos_teoricos[0].append(m * n)
        costos_teoricos[1].append(4**min(n,m))
        costos_teoricos[2].append(m + n)

    graficar(tiempos, "Terminal Inteligente")
    guardar_archivos(tiempos, ["Terminal_dinamica", "Terminal_fuerza_bruta", "Terminal_voraz"])
    guardar_archivos(costos_teoricos, ["Terminal_teorico_dinamica", "Terminal_teorico_fuerza_bruta", "Terminal_teorico_voraz"])

def tiempo_subasta():
    casos = [
        (100, 10, 0, [(10, 0, 100)]),
        (100, 10, 1, [(50, 10, 60), (10, 0, 100)]),
        (100, 10, 2, [(50, 10, 60), (45, 40, 80), (10, 0, 100)]),
        (100, 10, 3, [(50, 10, 60), (45, 40, 80), (30, 10, 30), (10, 0, 100)]),
        (100, 10, 4, [(50, 10, 60), (45, 40, 80), (30, 10, 30), (20, 10, 70), (10, 0, 100)]),
        ]
    
    costos_teoricos = [[], [], []]
    tiempos = [[], [], []]

    for caso in casos:
        result_dinamica = tiempo_ejecucion(subasta_dp, caso)
        result_fuerza_bruta = tiempo_ejecucion(subasta_fuerza_bruta, caso)
        result_voraz = tiempo_ejecucion(subasta_voraz, caso)
       

        tiempos[0].append(result_dinamica)
        tiempos[1].append(result_fuerza_bruta)
        tiempos[2].append(result_voraz)
        
        A, n = caso[0], caso[2]
        costos_teoricos[0].append(n + A**2)
        costos_teoricos[1].append(A**n)
        costos_teoricos[2].append((n * math.log(n))if n > 1 else n)

    graficar(tiempos, "Subasta")
    guardar_archivos(tiempos, ["Subasta_dinamica", "Subasta_voraz", "Subasta_fuerza_bruta"])
    guardar_archivos(costos_teoricos, ["Subasta_teorico_dinamica", "Subasta_teorico_voraz", "Subasta_teorico_fuerza_bruta"])

if __name__ == "__main__":
    tiempos_terminal_inteligente()
    tiempo_subasta()


