# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Méndez
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
# Escribí tu código acá
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


# 20. Maximiliano (cagaste)
# ---------------------------------
# Escribí tu código acá
# ---------------------------------
