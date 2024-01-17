

class Estudiante:
    def __init__(self, nombre=None, email=None, semestre=None
                 , cedula=None, edad=None):
        self._nombre = nombre
        self._email = email
        self._semestre = semestre
        self._cedula = cedula
        self._edad = edad


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        self._semestre = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'Estudiante: {self.__dict__.__str__()}'

if '__main__'==__name__:
    e =  Estudiante(nombre='Luis', email='luis@mail.com', semestre='Primer Semestre')
    print(e)