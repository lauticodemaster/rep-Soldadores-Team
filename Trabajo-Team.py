# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Méndez
# ---------------------------------

# ---------------------------------


# 2. Mailén Ortiz
# ---------------------------------
# prueba
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

# solicito el texto
texto = "La lluvia en Mendoza es escasa"

# obtengo el tamanño
tamano = len(texto)

# muestro el resultado
print("El tamaño de la cadena es:", tamano)
# ---------------------------------


# 7. Leonel Fachienlli
# ---------------------------------
cadena = input("Ingrese una cadena de texto: ")

# calculo el tamaño con len()
tamano = len(cadena)

# inicializo el contador de vocales
contador_vocales = 0

# recorro cada letra de la cadena
for letra in cadena:
    # pasar la letra a minúscula para simplificar la comparación
    letra = letra.lower()
    
    # si la letra es una vocal, sumar 1 al contador
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vocales = contador_vocales + 1

# muestro los resultados
print("El tamaño de la cadena es:", tamano)
print("La cantidad de vocales es:", contador_vocales)
# ---------------------------------


# 8. Mailén Ortiz
# ---------------------------------
# Escribí tu código acá
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
cadena = "hipopotamo"

# extraigo cuarta y quinta letra 
cuarta = cadena[3]
quinta = cadena[4]
#escribo las letras extraidas de la palabra 
print("Cuarta letra:", cuarta)
print("Quinta letra:", quinta)
# ---------------------------------


# 13. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 14. Mailén Ortiz
# ---------------------------------
# Escribí tu código acá
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
