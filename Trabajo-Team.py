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
# Algoritmo para sumar los 3 dígitos de un número de 3 cifras

# 1. Creamos la entrada de los datos 
numero = int(input("Ingrese un número de 3 dígitos (100 - 999): "))

# 2. sacamos los digitos de dígitos usando módulo y división entera
digito3 = numero % 10          # Último dígito
numero = numero // 10          # Quita el último dígito

digito2 = numero % 10          # Segundo dígito
numero = numero // 10          # Quita el segundo dígito

digito1 = numero % 10          # Primer dígito

# 3. Suma de los dígitos
suma = digito1 + digito2 + digito3

# 4. Salida
print("La suma de los dígitos es:", suma)

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
# cadena = "La lluvia en Mendoza es escasa"

# Definimos la cadena del ejercicio 6 
cadena = "La lluvia en Mendoza es escasa"

# Hacemos q el for lea toda la cadena letra por letra
for caracter in cadena:
    # La función ord() lo vuelve al  carácter en su valor ASCII
    # Con end=" " hacemos que se impriman en una sola línea separados por espacios y se lea mas facil
    print(ord(caracter), end=" ")


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

# En Python no hay variables de tipo valor como en Java. Todo en Python es un objeto y las variables apuntan a ese objeto en memoria. Si el objeto es inmutable (como números, strings o tuplas), cambiar otra variable que apunte al mismo objeto no lo afectae. Si el objeto es mutable (como listas o diccionarios), cualquier cambio desde una variable afecta a las demás que apuntan al mismo objeto.

# ---------------------------------


# 15. Maximiliano
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 16. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 17/18 Luciano Nicolas Ibañez
# ---------------------------------
from datetime import date

class FuncionesPrograma:

    @staticmethod
    def getFechaString(fecha: date) -> str:
        # Ponemos el nombre de cada numero en formato cadena
        dias = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince",
            16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve", 20: "Veinte",
            21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco",
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta",
            31: "Treinta y uno"
        }

        # Anotamos los meses pa
        meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        # Anotamos algunos años comunes(podemos todos pero nos quedamos aca hasta el año q viene)
        anios = {
            1900: "mil novecientos",
            1910: "mil novecientos diez",
            1920: "mil novecientos veinte",
            1930: "mil novecientos treinta",
            1940: "mil novecientos cuarenta",
            1950: "mil novecientos cincuenta",
            1960: "mil novecientos sesenta",
            1970: "mil novecientos setenta",
            1980: "mil novecientos ochenta",
            1990: "mil novecientos noventa",
            2000: "dos mil",
            2010: "dos mil diez",
            2020: "dos mil veinte",
            2024: "dos mil veinticuatro"
        }

        # Las convertimos para q sea parte de la fecha y de un retorno mejor
        dia_str = dias[fecha.day]
        mes_str = meses[fecha.month]
        anio_str = anios[fecha.year]

        return f"{dia_str} de {mes_str} de {anio_str}"

    @staticmethod #Método que se usa para que la función solo realice una tarea y no modifique ni use datos externos de la clase o instancia
    def getFechaDate(dia: int, mes: int, anio: int) -> date:
        return date(anio, mes, dia)

#Todo lo q es la rama principal donde va a retornar todo tanto la fecha como cadena y los datos q pide el usuario
class Principal:
    @staticmethod
    def main():
        # Pedir fecha al usuario
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        # Crear fecha y mostrar en cadena
        fecha = FuncionesPrograma.getFechaDate(dia, mes, anio)
        print("Tu fecha convertida:", FuncionesPrograma.getFechaString(fecha))


if __name__ == "__main__":
    Principal.main()



# ---------------------------------


# 19. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 20. Maximiliano (cagaste)
# ---------------------------------
# Escribí tu código acá
# ---------------------------------
