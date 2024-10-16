import time
import numpy as np
import matplotlib.pyplot as plt

from Terminal_inteligente.dinamica import terminal_inteligente
from Terminal_inteligente.fuerza_bruta import fuerza_bruta
from Terminal_inteligente.voraz import programacion_voraz

def tiempo_ejecucion(funcion, args):
    array = np.zeros(50)
    for i in range(50):
        inicio = time.time()
        funcion(*args)
        fin = time.time()
        array[i] = fin - inicio
    return np.mean(array)


casos = [
    ("Ay", "Ya"),
    ("Pal", "Pup"),
    ("Mora", "More"),
    ("Agua", "Vaca"),
    ("Destino", "Caminos"),
    ("francesa", "ancestro"),
    ("ingenioso", "ingeniero"),
]

tiempos = [[], [], []]

for caso in casos:
    result_dinamica = tiempo_ejecucion(terminal_inteligente, caso)
    result_fuerza_bruta = tiempo_ejecucion(fuerza_bruta, caso)
    result_voraz = tiempo_ejecucion(programacion_voraz, caso)

    tiempos[0].append(result_dinamica)
    tiempos[1].append(result_fuerza_bruta)
    tiempos[2].append(result_voraz)

def graficar (tiempos):
    plt.figure(figsize = (10, 5))
    plt.title("Tiempo de ejecución")
    plt.plot(tiempos[0], label="Programación dinámica")
    plt.plot(tiempos[1], label="Fuerza bruta")
    plt.plot(tiempos[2], label="Programación voraz")
    plt.legend()
    plt.yscale("log")
    plt.savefig("tiempos.png")

graficar(tiempos)