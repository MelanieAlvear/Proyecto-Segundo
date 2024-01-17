import pyodbc
from Datos.conexion import Conexion
from Dominio.estudiante import Estudiante

# --Integrantes--
# Melanie Alvear Ortiz
# Eileen Gonzáles Arias
# Lilibeth Bennett Rezabala
# Karelin Correa Plúas

class EstudianteDao:
    _INSERTAR_ESTUDIANTE = (
        "INSERT INTO Estudiantes (nombre, cedula, semestre, email, edad, estatura, peso, fecha_nacimiento) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    )
    _SELECCIONAR_X_CEDULA = (
        "SELECT NOMBRE, CEDULA, SEMESTRE, EMAIL, EDAD, ESTATURA, PESO, FECHA_NACIMIENTO FROM Estudiantes "
        "WHERE CEDULA = ?"
    )
    _SELECCIONAR_PERSONAS = (
        "SELECT NOMBRE, CEDULA, SEMESTRE, EMAIL, EDAD, ESTATURA, PESO, FECHA_NACIMIENTO FROM Estudiantes"
    )

    @classmethod
    def insertar_estudiante(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    estudiante.nombre,
                    estudiante.cedula,
                    estudiante.semestre,
                    estudiante.email,
                    estudiante.edad,
                    estudiante.estatura,
                    estudiante.peso,
                    estudiante.fecha_nacimiento,
                )
                cursor.execute(cls._INSERTAR_ESTUDIANTE, datos)
        except Exception as e:
            print(e)

    @classmethod
    def seleccionar_x_cedudla(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                estudiante_encontrado = resultado.fetchone()
                estudiante.cedula = estudiante_encontrado[1]
                estudiante.nombre = estudiante_encontrado[0]
                estudiante.email = estudiante_encontrado[3]
                estudiante.semestre = estudiante_encontrado[2]
                estudiante.edad = estudiante_encontrado[4]
                estudiante.estatura = estudiante_encontrado[5]
                estudiante.peso = estudiante_encontrado[6]
                estudiante.fecha_nacimiento = estudiante_encontrado[7]
                return estudiante
        except Exception as e:
            print(e)
            estudiante = None

    @classmethod
    def seleccionar_personas(cls):
        try:
            estudiantes = list()
            with Conexion.obtenerCursor() as cursor:
                registros = cursor.execute(cls._SELECCIONAR_PERSONAS).fetchall()
                for registro in registros:
                    estudiante = Estudiante(
                        nombre=registro[0],
                        cedula=registro[1],
                        email=registro[3],
                        semestre=registro[2],
                        edad=registro[4],
                        estatura=registro[5],
                        peso=registro[6],
                        fecha_nacimiento=registro[7],
                    )
                    estudiantes.append(estudiante)
                return estudiantes
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    personas = EstudianteDao.seleccionar_personas()
    for persona in personas:
        print(persona)