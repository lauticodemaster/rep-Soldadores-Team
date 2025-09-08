# Escribe un programa que calcule la suma de todos los elementos en una lista 
# bidimensional - Mailen Ortiz

lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

# for fila in lista: #recorre cada fila de la lista
#     for elemento in fila: #recorre cada elemento de la fila
#         suma += elemento

suma = sum(sum(fila) for fila in lista)

print(suma)