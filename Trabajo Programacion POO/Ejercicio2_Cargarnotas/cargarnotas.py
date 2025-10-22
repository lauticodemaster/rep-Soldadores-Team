from alumno import Alumno
from nota import Nota

def main():
    alumnos = []
    
    while True:
        print("INGRESE DATOS DEL ALUMNO")
        nombre = input("Ingrese nombre completo: ")

        # Validar nombre repetido
        existe_nombre = False
        for a in alumnos:
            if a.nombreCompleto == nombre:
                existe_nombre = True
                break
        if existe_nombre:
            print("El nombre ya existe, intente otro.")
            continue

        legajo = input("Ingrese legajo (5 dígitos): ")
        if len(legajo) != 5 or not legajo.isdigit():
            print("El legajo debe tener 5 dígitos.")
            continue

        # Validar legajo repetido
        existe_legajo = False
        for a in alumnos:
            if a.legajo == int(legajo):
                existe_legajo = True
                break
        if existe_legajo:
            print("El legajo ya existe, intente otro.")
            continue

        alumno = Alumno(nombre, int(legajo))

        # Carga de notas
        while True:
            print("INGRESE NOTA DEL ALUMNO")
            catedra = input("Ingrese nombre de cátedra: ")
            try:
                notaExamen = float(input("Ingrese nota (1-10): "))
                if notaExamen < 1 or notaExamen > 10:
                    print("Nota fuera de rango.")
                    continue
            except:
                print("Ingrese un número válido.")
                continue

            nota = Nota(catedra, notaExamen)
            alumno.agregar_nota(nota)

            salirNotas = input("Desea salir de la carga de notas? (s/n): ")
            if salirNotas.lower() == "s" and len(alumno.notas) >= 1:
                break
            elif salirNotas.lower() == "s" and len(alumno.notas) == 0:
                print("Debe ingresar al menos una nota.")

        alumnos.append(alumno)

        salirAlumno = input("Desea salir de carga de alumnos? (s/n): ")
        if salirAlumno.lower() == "s":
            break

    # Mostrar datos
    print("\n--- INFORMACIÓN DE ALUMNOS ---")
    for a in alumnos:
        print("Alumno:", a.nombreCompleto, "| Legajo:", a.legajo)
        for n in a.notas:
            print("Cátedra:", n.catedra, "| Nota:", n.notaExamen)
        print("Promedio:", a.calcular_promedio())
        print("-----------------------------")

if _name_ == "_main_":
    main()