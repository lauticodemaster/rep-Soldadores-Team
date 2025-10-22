from alumno import Alumno
from nota import Nota

def main():
    alumnos = []

    while True:
        print("\n--- INGRESE DATOS DEL ALUMNO ---")

        nombre = input("Ingrese nombre completo: ")
        if not all(c.isalpha() or c.isspace() for c in nombre):
            print("El nombre solo puede contener letras y espacios.")
            continue

        if any(a.nombreCompleto == nombre for a in alumnos):
            print("El nombre ya existe, intente otro.")
            continue

        legajo = input("Ingrese legajo (5 dígitos): ")
        if not legajo.isdigit() or len(legajo) != 5:
            print("El legajo debe tener exactamente 5 dígitos numéricos.")
            continue

        if any(a.legajo == int(legajo) for a in alumnos):
            print("El legajo ya existe, intente otro.")
            continue

        alumno = Alumno(nombre, int(legajo))

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

            salirNotas = input("¿Desea salir de la carga de notas? (s/n): ").lower()
            if salirNotas == "s":
                if len(alumno.notas) >= 1:
                    break
                else:
                    print("Debe ingresar al menos una nota antes de salir.")

        alumnos.append(alumno)

        salirAlumno = input("\n¿Desea salir de carga de alumnos? (s/n): ").lower()
        if salirAlumno == "s":
            break

    print("\n--- INFORMACIÓN DE ALUMNOS ---")
    for a in alumnos:
        print("\nAlumno:", a.nombreCompleto, "| Legajo:", a.legajo)
        for n in a.notas:
            print("Cátedra:", n.catedra, "| Nota:", n.notaExamen)
        print("Promedio:", round(a.calcular_promedio(), 2))
        print("-----------------------------")


if __name__ == "__main__":
    main()
