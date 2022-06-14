import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("radio-checkbox.ui", self)
        self.radio_value() #llamado a funcion
        self.boton.clicked.connect(self.radio_value) #accion que ejecuta el evento
        self.checkbox_state()
        self.boton.clicked.connect(self.checkbox_state)

    def radio_value(self):
        if self.python.isChecked():
            self.labelLenguaje.setText("Python ha sido seleccionado")
        elif self.PHP.isChecked():
            self.labelLenguaje.setText("PHP ha sido seleccionado")
        elif self.perl.isChecked():
            self.labelLenguaje.setText("Perl ha sido seleccionado")
        elif self.ruby.isChecked():
            self.labelLenguaje.setText("rubi ha sido seleccionado")
        else:
            self.labelLenguaje.setText("no hay seleccionado ningun leguaje")

    def checkbox_state(self):
        if self.terminos.isChecked():
            self.labelTerminos.setText("Has aceptado los términos")
        else:
            self.labelTerminos.setText("No has aceptado los términos")



app = QApplication(sys.argv)
dialogo = Dialogo()  #objeto de clase Dialogo
dialogo.show()
app.exec_()
