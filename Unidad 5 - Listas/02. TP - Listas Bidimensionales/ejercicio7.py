# Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
# cuadrada. - Maximiliano Mendez

# Pedir el tamaño de la matriz cuadrada
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Crear la matriz vacía
matriz = []

# En esta sección puse un bucle for anidado con un bucle while para llenar la matrizz
for i in range(n):  # El rango de la matriz
    while True:
        # Ingreso de la fila con validación
        fila = input(f"Ingrese los {n} elementos de la fila {i+1} separados por espacio: ").split()
        if len(fila) != n:
            print(f"Debe ingresar exactamente {n} elementos.")
            continue
        # Convertimos los elementos de la fila a enteros
        fila = [int(x) for x in fila]
        break
    matriz.append(fila)

# Extraer la diagonal principal usando IF
diagonal = []
for i in range(n):
    for j in range(n):
        if i == j:  # condición de la diagonal principal
            diagonal.append(matriz[i][j])

# Los mostramos 
print("Elementos de la diagonal principal:", diagonal)
