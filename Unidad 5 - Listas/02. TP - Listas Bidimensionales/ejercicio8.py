# Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad 
# es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto 
# son 0. - Mailen Ortiz

import numpy as np

tamañoMatriz = int(input("Ingrese el tamaño de la matriz identidad:"))

matrizIdentidad =  [[1 if i == j else 0 for j in range(tamañoMatriz)] for i in range(tamañoMatriz)]

for fila in matrizIdentidad:
    print(fila)
