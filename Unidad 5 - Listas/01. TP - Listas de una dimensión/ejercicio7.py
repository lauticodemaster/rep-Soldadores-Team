# Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
# promedio de los elementos - Lautaro Fernández


# Pedimos al usuario que ingrese los números separados por espacio
entrada = input("Ingresa una lista de números separados por espacio: ")

# Separamos los números como texto
numeros_texto = entrada.split()

# Convertimos cada número de texto a entero y los guardamos en una lista
numeros = []
for n in numeros_texto:
    numeros.append(int(n))

# Sumamos todos los números usando un bucle
suma_total = 0
for num in numeros:
    suma_total += num

# Calculamos el promedio (suma total dividido la cantidad de números)
promedio = suma_total / len(numeros)

# Mostramos el resultado al usuario
print("El promedio de los números es:", promedio)
