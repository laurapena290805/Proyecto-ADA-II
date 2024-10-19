import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def leer_archivo_array(nombre_archivo, ruta="./tiempos/"):
    with open(ruta + nombre_archivo + '.txt', 'r') as f:
        lineas = f.readlines()
        arr = np.array([float(l) for l in lineas])
    return arr

def normalizar(arr):
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

def graficar_interpolacion(x, y, nombre_grafica="Interpolación"):
    # Normalizar los datos
    x_norm = normalizar(x)
    y_norm = normalizar(y)

    # Crear el objeto de interpolación lineal
    f_linear = interpolate.interp1d(x_norm, y_norm)

    # Crear el objeto de interpolación cúbica (si prefieres una curva suave)
    f_cubic = interpolate.interp1d(x_norm, y_norm, kind='cubic')

    # Nuevos puntos para estimar los valores (interpolación)
    x_new = np.linspace(min(x_norm), max(x_norm), 100)  # Ajustamos el rango de x_new
    y_linear = f_linear(x_new)
    y_cubic = f_cubic(x_new)

    # Graficar los puntos originales y las líneas de tendencia
    plt.plot(x_norm, y_norm, 'o', label='Puntos originales')
    plt.plot(x_new, y_linear, '-', label='Interpolación lineal')
    plt.plot(x_new, y_cubic, '--', label='Interpolación cúbica')
    plt.legend()
    plt.savefig('./graficas/' + nombre_grafica + '.png')
    plt.close()

# Ejecutar para cada conjunto de datos



def graficar_terminal_interpolacion():

    ruta_datos = [
        ('terminal_teorico_dinamica', 'terminal_dinamica' , 'interpolacion_terminal_dinamica'),
        ('terminal_teorico_fuerza_bruta', 'terminal_fuerza_bruta', 'interpolacion_terminal_fuerza_bruta'),
        ('terminal_teorico_voraz', 'terminal_voraz', 'interpolacion_terminal_voraz'),
    ]
    for ruta in ruta_datos:
        costos_teoricos = leer_archivo_array(ruta[0])
        tiempos = leer_archivo_array(ruta[1])
        graficar_interpolacion(costos_teoricos, tiempos, nombre_grafica=ruta[2])

def graficar_subasta_interpolacion():
    pass