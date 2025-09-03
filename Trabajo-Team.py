# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Méndez
# ---------------------------------

# ---------------------------------


# 2. Mailén Ortiz
# ---------------------------------

# Si se asigna un valor a una variable fuera del rango permitido y el programa no tiene ninguna verificación, el código va a seguir ejecutándose normalmente pero va a generarse un error lógico, aunque no aparezca un mensaje específico de error cuando lo ejecutemos en la terminal. Para evitarlo, se debe validar el valor usando condicionales que, en el caso que sea un valor fuera de rango, muestre un mensaje de error y vuelva a pedir el dato hasta que esté dentro del rango correcto.

#Ejemplo: Si en un bucle se ingresa un valor fuera del rango estipulado este va a generar un mensaje de error y va a pedirle al usuario volver a ingresar un número dentro del rango.

nota = -3 #Se le da un valor fuera de rango para que entre al bucle While 

while (nota < 1) or (nota > 10):
    nota = int(input("Ingrese una nota en el rango del 1 al 10:")) #Se ingresa una nueva nota

    if (nota >= 1) and (nota <= 10): #Verifica si está en el rango, si no lo está vuelve a ejecutarse el bucle.
        print("Nota ingresada correctamente")
    else:
        print(f"La nota ingresada: {nota}, no es válida. Ingrese una nota en el rango del 1 al 10")

# ---------------------------------


# 3. Nicolás Ibañez
# ---------------------------------

# ---------------------------------


# 4. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 5. Maximiliano
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 6. Leonel Fanchinelli
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 7. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 8. Mailén Ortiz
# ---------------------------------

frase = input("Ingrese una frase: ")
nuevaPalabra = "" #Variable vacía donde se almacenará la nueva palabra

for letra in frase: #Recorre cada letra de la frase
    if letra.lower() == "a": #En el caso de ser mayúscula la transforma en minúscula.
        nuevaPalabra += "e" #Remplaza la "a" por una "e"
    else:
        nuevaPalabra += letra #Si no la deja igual 

print(nuevaPalabra) 

# ---------------------------------


# 9. Nicolás Ibañez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 10. Maximiliano
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 11. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 12. Leonel Fanchinelli
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 13. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 14. Mailén Ortiz
# ---------------------------------




# ---------------------------------


# 15. Maximiliano
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 16. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 17. Leonel Fanchinelli
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 18. Nicolás Ibañez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 19. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 20. Maximiliano (cagaste)
# ---------------------------------
# Escribí tu código acá
# ---------------------------------
