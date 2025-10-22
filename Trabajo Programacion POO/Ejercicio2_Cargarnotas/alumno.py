from nota import Nota

class Alumno:
    def _init_(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        suma = 0
        for n in self.notas:
            suma = suma + n.notaExamen
        promedio = suma / len(self.notas)
        return promedio