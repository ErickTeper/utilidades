import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import ctypes

from sympy import false
#permite obtener tamaños del escritorio, pantalla


# Clase heredad de QMainWindow (constructor de ventanas)

class Ventana(QMainWindow):
    # Método constructor de la clase
    def __init__(self):
        #çIniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #cargar la configuracion del archivo.ui en el objeto
        uic.loadUi("MainWindow.ui", self)
        #cambiar título
        self.setWindowTitle("Balance")
        #mostrar la ventana maximizada
        self.showMaximized()
        #fijar el tamaño de la ventana
        #fijar tamaño minimo
        self.setMinimumSize(500, 500)
        #fijar el tamaño maximo
        self.setMaximumSize(500, 500)
        #Mover la ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2)-(self.frameSize().height() / 2)
        self.move(int(left), int(top))
        #desactivar la ventana
        """self.setEnabled(False)"""
        #Asignar un tipo de fuente
        qfont = QFont("Arial", 12, QFont.Bold)
        self.setFont(qfont)
        #Asignar un tipo de cursor
        self.setCursor(Qt.SizeAllCursor)
        #asignar estilos CSS
        self.setStyleSheet("background-color:#00ff00")
        self.boton.setStyleSheet("background-color: #ff0000; color: #ffffff ")

    #QEvent eventos de PyQT
    def showEvent(self, event):
        self.bienvenido.setText("¡¡¡bienvenido!!!")
    
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "salir...", "¿seguro quiere salir de la aplicacion?",
        QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()

    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.posicion.setText("X: " + x + " Y: "+ y)


#instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#MOstrar la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()
