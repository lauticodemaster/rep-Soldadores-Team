# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Mendez
# ---------------------------------
#CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la 
#--conversión. Muestre por pantalla el resultado de las conversiones.  
valorDecimal = int(input("Ingrese un numero decimal: ")) #decimal
print(valorDecimal, type(valorDecimal)) 
valorString = str(valorDecimal)#string
print(valorString, type(valorString))
valorBool = bool(valorDecimal)#bool
print(valorBool, type(valorBool))
valorFloat = float(valorDecimal)#float
print(valorFloat, type(valorFloat))
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


# 5. Maximiliano Reinoso
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
# pido la cadena al usuario
cadena = input("Ingrese una cadena de texto: ")

# calculo el tamaño de la cadena
tamano = len(cadena)

# cuento las vocales
contador_vocales = 0
for caracter in cadena.lower():   # .lower() convierte todo a minúsculas
    if caracter in "aeiou":
        contador_vocales += 1

# muestro los resultados
print("El tamaño de la cadena es:", tamano)
print("La cantidad de vocales es:", contador_vocales)
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


# 10. Maximiliano Reinoso
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


# 13. Maximiliano Mendez
# ---------------------------------
#Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera.  
cadena1 = input("Ingrese la primera Cadena: ")
cadena2 = input("Ingrese la Segunda Cadena: ")
#Le preguntamos a la maquina si encuentra la cadena 2 en la 1
if cadena1.find(cadena2) == -1:
    print("La segunda cadena NO se encontro en la primera")
else:
    print("La segunda cadena se encontro en la primera")

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


# 19. Maximiliano Mendez
# ---------------------------------
# #cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un #atributo de nombre operación. 
#Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:  
#sumarNumeros() 
#restarNumeros() 
#multiplicarNumeros() 
#dividirNumeros() 
#El quinto método será el siguiente:  
#aplicarOperacion(operacion){  
#…………………..  
#}  
#Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
#clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
#ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
#”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las 
#operaciones.  
class OperacionMatematica:
    #hacemos la clase para realizar operaciones matematicas
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 == 0:
            return "Error: No se puede dividir por cero."
        return self.valor1 / self.valor2

    def aplicarOperacion(self, operacion):
        #Esto aplica una operación matemática basada en los símbolo correspondientes.
        #Parámetros:
        #Los simbolos en forma string de la operación ('+', '-', '*', '/').
        operaciones = {
            '+': self.sumarNumeros,
            '-': self.restarNumeros,
            '*': self.multiplicarNumeros,
            '/': self.dividirNumeros,
        }
        
        if operacion in operaciones:
            return operaciones[operacion]()
        else:
            return "Error: Operación no válida."

# Inicio del programa 
if __name__ == "__main__":
    # Creamos una instancia de OperacionMatematica con los valores 10 y 24
    operacion = OperacionMatematica(10, 24)

    # Definimos una lista con los símbolos de las operaciones a realizar
    simbolos_operaciones = ['+', '-', '*', '/']

    # Iteramos sobre la lista para aplicar cada operación
    for simbolo in simbolos_operaciones:
        resultado = operacion.aplicarOperacion(simbolo)
        print(f"El resultado de la operación '{simbolo}' es: {resultado}")
# ---------------------------------


# 20. Maximiliano Reinoso
# ---------------------------------
# Escribí tu código acá
# ---------------------------------
