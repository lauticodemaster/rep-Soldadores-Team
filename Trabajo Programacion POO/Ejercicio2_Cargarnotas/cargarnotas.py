from alumno import Alumno
from nota import Nota

def main():
    alumnos = []

    while True:
        print("\n--- INGRESE DATOS DEL ALUMNO ---")
        nombre = input("Ingrese nombre completo: ")

        # Validar que el nombre solo tenga letras y espacios
        es_valido = True
        for c in nombre:
            if not (c.isalpha() or c == " "):
                es_valido = False
                break
        if not es_valido or nombre.strip() == "":
            print("El nombre solo puede contener letras y espacios.")
            continue

        # Validar nombre repetido
        nombre_repetido = False
        for a in alumnos:
            if a.nombreCompleto.lower() == nombre.lower():
                nombre_repetido = True
                break
        if nombre_repetido:
            print("El nombre ya existe, intente otro.")
            continue

        legajo = input("Ingrese legajo (5 dígitos): ")
        if len(legajo) != 5 or not legajo.isdigit():
            print("El legajo debe tener 5 dígitos.")
            continue

        # Validar legajo repetido
        legajo_repetido = False
        for a in alumnos:
            if a.legajo == int(legajo):
                legajo_repetido = True
                break
        if legajo_repetido:
            print("El legajo ya existe, intente otro.")
            continue

        alumno = Alumno(nombre, int(legajo))

        # Carga de notas
        while True:
            print("\n--- INGRESE NOTA DEL ALUMNO ---")
            catedra = input("Ingrese nombre de cátedra: ")

            try:
                notaExamen = float(input("Ingrese nota (1-10): "))
                if notaExamen < 1 or notaExamen > 10:
                    print("La nota debe estar entre 1 y 10.")
                    continue
            except ValueError:
                print("Ingrese un número válido.")
                continue

            nota = Nota(catedra, notaExamen)
            alumno.agregar_nota(nota)

            salirNotas = input("Desea salir de la carga de notas? (s/n): ")
            if salirNotas.lower() == "s":
                if len(alumno.notas) >= 1:
                    break
                else:
                    print("Debe ingresar al menos una nota.")

        alumnos.append(alumno)

        salirAlumno = input("\nDesea salir de carga de alumnos? (s/n): ")
        if salirAlumno.lower() == "s":
            break

    # Mostrar datos
    print("\n--- INFORMACIÓN DE ALUMNOS ---")
    for a in alumnos:
        print("\nAlumno:", a.nombreCompleto, "| Legajo:", a.legajo)
        for n in a.notas:
            print("Cátedra:", n.catedra, "| Nota:", n.notaExamen)
        print("Promedio:", a.calcular_promedio())
        print("-----------------------------")

main()