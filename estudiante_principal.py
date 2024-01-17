from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Datos.estudiante_Dao import EstudianteDao
from Dominio.estudiante import Estudiante
from GUI.vtn_principal import Ui_vtn_principal


class EstudianteServicio(QMainWindow):
    def __init__(self):
        super(EstudianteServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.estudiante = None
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_busca_x_cedula.clicked.connect(self.buscar_por_cedula)
        self.ui.btn_calcular.clicked.connect(self.calcular)
        self.ui.txt_cedula.setValidator(QIntValidator())
        self.ui.txt_edad.setValidator(QIntValidator())
        regex = QRegularExpression("^\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b$")
        validator = QRegularExpressionValidator(regex)
        self.ui.txt_email.setValidator(validator)


    def grabar(self):
        if self.validar_datos():
            nombre = self.ui.txt_nombre.text().capitalize()
            email = self.ui.txt_email.text().lower()
            semestre = self.ui.cb_semestre.currentText()
            cedula = self.ui.txt_cedula.text()
            edad = self.ui.txt_edad.text()
            self.estudiante = Estudiante(nombre=nombre, email=email, semestre=semestre
                                         , cedula=cedula, edad=edad)

            try:
                EstudianteDao.insertar_estudiante(self.estudiante)
            #     with open('estudiante.txt', 'a') as archivo:
            #         archivo.write(self.estudiante.__str__())
            #         archivo.write('\n')
                self.ui.sb_estado.showMessage('Ingreso exitoso.',3000)
                self.ui.txt_email.setText('')
                self.ui.txt_nombre.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_edad.setText('')
                self.ui.cb_semestre.setCurrentText('Seleccionar')
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'No se pudo grabar.')
                print(e)
        else:
                QMessageBox.warning(self, 'Advertencia', 'Falta ingresar datos.')

    def validar_datos(self):
        return (len(self.ui.txt_nombre.text()) > 0
                and len(self.ui.txt_email.text()) > 0
                and self.ui.cb_semestre.currentText()!='Seleccionar'
                and len(self.ui.txt_cedula.text())==10
                and len(self.ui.txt_edad.text())>0)


    def buscar_por_cedula(self):
        cedula = self.ui.txt_cedula.text()
        self.estudiante = Estudiante(cedula=cedula)
        estudiante_encontrado = EstudianteDao.seleccionar_x_cedudla(self.estudiante)
        # print(estudiante_encontrado)
        self.ui.txt_email.setText(estudiante_encontrado.email)
        self.ui.txt_nombre.setText(estudiante_encontrado.nombre)
        self.ui.txt_edad.setText(estudiante_encontrado.edad)
        self.ui.cb_semestre.setCurrentText(estudiante_encontrado.semestre)

    def calcular(self):
        estudiantes = EstudianteDao.seleccionar_personas()
        total_edad = 0
        total_estudiantes = 0
        for estudiante in estudiantes:
            if estudiante.edad:
                total_edad += estudiante.edad
                total_estudiantes += 1
        promedio = total_edad / total_estudiantes
        print(f'El promedio de edad de los estudianetes: {promedio}')