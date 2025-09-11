# Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
# suma de todos los elementos en la lista - Lautaro Fernández


# Paso 1: Pedimos al usuario que ingrese números separados por espacios
entrada = input("Ingresa una lista de números separados por espacio: ")

# Paso 2: Convertimos la entrada (string) en una lista de números
# - split() separa el texto por espacios
# - map(int, ...) convierte cada pedacito en número entero
numeros = list(map(int, entrada.split()))

# Paso 3: Calculamos la suma de todos los elementos con la función sum()
suma_total = sum(numeros)

# Paso 4: Mostramos el resultado
print("La suma de los números es:", suma_total)
