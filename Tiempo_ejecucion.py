import time
import numpy as np
import matplotlib.pyplot as plt

from Terminal_inteligente.dinamica import terminal_inteligente
from Terminal_inteligente.fuerza_bruta import fuerza_bruta
from Terminal_inteligente.voraz import programacion_voraz
from Subasta_publica.dinamica import subasta_dp
from Subasta_publica.voraz import subasta_voraz

def tiempo_ejecucion(funcion, args):
    array = np.zeros(50)
    for i in range(50):
        inicio = time.time()
        funcion(*args)
        fin = time.time()
        array[i] = fin - inicio
    return np.mean(array)

def graficar (tiempos):
    plt.figure(figsize = (10, 5))
    plt.title("Tiempo de ejecución")
    plt.plot(tiempos[0], label="Programación dinámica")
    plt.plot(tiempos[1], label="Fuerza bruta")
    plt.plot(tiempos[2], label="Programación voraz")
    plt.legend()
    plt.yscale("log")
    plt.savefig("tiempos.png")

def guardar_tiempos(tiempos, l_archivos):
    
    for i in range(len(tiempos)):
        tiempo = tiempos[i]
        archivo = l_archivos[i] + ".txt"
        with open("./Tiempos/" + archivo, "w") as f:
            for t in tiempo:
                f.write(f"{t}\n")

def tiempos_terminal_inteligente():
    casos = [
        ("Ay", "Ya"),
        ("Pal", "Pup"),
        ("Mora", "More"),
        ("Agua", "Vaca"),
        ("Destino", "Caminos"),
    ]

    tiempos = [[], [], []]

    for caso in casos:
        result_dinamica = tiempo_ejecucion(terminal_inteligente, caso)
        result_fuerza_bruta = tiempo_ejecucion(fuerza_bruta, caso)
        result_voraz = tiempo_ejecucion(programacion_voraz, caso)

        tiempos[0].append(result_dinamica)
        tiempos[1].append(result_fuerza_bruta)
        tiempos[2].append(result_voraz)

    graficar(tiempos)
    guardar_tiempos(tiempos, ["Terminal_dinamica", "Terminal_fuerza_bruta", "Terminal_voraz"])

def tiempo_subasta():
    casos = [
        (1000, 100, 2 , [(500, 100, 600), (450, 400, 800), (100, 0, 1000)]),
        (1000, 100, 1, [(500, 100, 600), (100, 0, 1000)]),
        (1000, 100, 0, [(100, 0, 1000)]),
        (1000, 100, 3, [(500, 100, 600), (450, 400, 800), (300, 100, 300), (100, 0, 1000)]),
        (1000, 100, 3, [(500, 400, 600), (100, 400, 800), (200, 100, 700), (100, 0, 1000)]),
        ]
    
    tiempos = [[], [], []]

    for caso in casos:
        result_dinamica = tiempo_ejecucion(subasta_dp, caso)
        result_voraz = tiempo_ejecucion(subasta_voraz, caso)

        tiempos[0].append(result_dinamica)
        tiempos[1].append(result_voraz)

    graficar(tiempos)
    guardar_tiempos(tiempos, ["Subasta_dinamica", "Subasta_voraz"])
       
if __name__ == "__main__":
    tiempos_terminal_inteligente()
    tiempo_subasta()
