# Escribe un programa que permita al usuario ingresar una lista y la invierta - Mailen Ortiz

lista = [] #Lista vacía para que luego el usuario ingrese los valores y se guarden acá
cantidadElementos = int(input("Ingrese la cantidad de elementos que quiere agregar: "))

for contador in range(cantidadElementos):
    elemento = input(f"Ingrese el elemento {contador +1}: ") #El usuario ingresa el valor
    lista.append(elemento) #El valor se guarda en la lista anteriormente vacía 

lista.reverse() #Invierte la lista creada 

print(f"Lista Invertida: {lista}")


