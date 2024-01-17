import sys

from PySide6.QtWidgets import QApplication

from Servicio.estudiante_principal import EstudianteServicio

app = QApplication()
vtn_principal = EstudianteServicio()
vtn_principal.show()
sys.exit(app.exec())