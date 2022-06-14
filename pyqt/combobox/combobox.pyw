import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("combobox.ui", self)
        self.boton.clicked.connect(self.getItem)

    #agregar nuevo item
        """self.lenguajes.addItem("C++")"""
    #eliminar item (elimina python en este ejemplo)
        self.lenguajes.removeItem(0)

    def getItem(self):
        item = self.lenguajes.currentText()
        self.labelLenguajes.setText("Has selecciona: " + item)

app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()