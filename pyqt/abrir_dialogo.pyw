import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self) #inicia el objeto
        self.resize(300, 300)
        self.setWindowTitle("Cuadro de dialogo")
        self.etiqueta = QLabel(self) #crea objeto etiqueta label para este cuadro de dialogo
        uic.loadUi("hoja_de_estilo.ui", self)
    
class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600, 600)
        self.setWindowTitle("ventana principal")
        self.boton = QPushButton(self) #crea el boton
        self.boton.setText("Abrir cuadro de dialogo")
        self.boton.resize(200, 30)
        self.dialogo = Dialogo()
        #capturar clic
        self.boton.clicked.connect(self.abrirDialogo)
    
    def abrirDialogo(self):
        self.dialogo.etiqueta.setText("Dialogo abierto desde la ventana principal")
        self.dialogo.exec_()

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()