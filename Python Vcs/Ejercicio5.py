
class Alumno:

    _aprueba = True
    _deficiente = False

    nombre = "Luis Felipe"
    nota = "Su Nota es 10.0 es Excelente para Quimica"

    nombre1 = "Laura Maria"
    nota1 = "Su Nota es 4.0 es Deficiente para Quimica"

    def aprueba(self):
        self._aprueba = True

    def deficiente(self):
        self._deficiente = False


Estudiante = Alumno()
print(Alumno.nombre, Alumno.nota)
print(Alumno.nombre1, Alumno.nota1)