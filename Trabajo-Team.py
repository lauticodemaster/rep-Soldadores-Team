# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Méndez
# ---------------------------------

# ---------------------------------


# 2. Mailén Ortiz
# ---------------------------------

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
# Escribí tu código acá
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


# 17. Leonel Fanchinelli
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 18. Nicolás Ibañez
# ---------------------------------
from datetime import date

class FuncionesPrograma:
    @staticmethod
    def get_fecha_date(dia, mes, anio):
        """
        Retorna un objeto date si la fecha es válida,
        sino lanza una excepción ValueError.
        """
        return date(anio, mes, dia)

def main():
    while True:
        try:
            # Pedir al usuario que ingrese la fecha
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            # Intentar crear la fecha usando el método estático
            fecha = FuncionesPrograma.get_fecha_date(dia, mes, anio)
            break  # Sale del bucle si la fecha es válida

        except ValueError:
            print("Fecha inválida. Por favor, ingrese un día, mes y año correctos.\n")
    
    print("La fecha ingresada es:", fecha)

if __name__ == "__main__":
    main()


# ---------------------------------


# 19. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 20. Maximiliano (cagaste)
# ---------------------------------
# Escribí tu código acá
# ---------------------------------
