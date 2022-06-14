import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat, startfile
from mimetypes import MimeTypes


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("treewidget.ui", self)
        self.boton.clicked.connect(self.getDir)
        self.directorio.itemDoubleClicked.connect(self.openElement)

    def getDir(self):
        #eliminar las filas de la busqueda anterior
        self.directorio.clear()
        #ruta indicada por el usuario
        dir = self.ruta.text()
        #si se trata de un directorio
        if path.isdir(dir):
        #recorrer sus elementos
            for element in listdir(dir):
                name = element
                pathinfo = dir + "\\" + name
                informacion = stat(pathinfo)
                #si es un directorio 
                if path.isdir(pathinfo):
                    type = "Carpeta de archivos"
                    size = ""
                else:
                    mime = MimeTypes()
                    #para saber el tipo de archivo (regresa dos elementos)
                    type = mime.guess_type(pathinfo)[0]
                    size = str(informacion.st_size) + "bytes"
                #Fecha de modificación
                date = str(time.ctime(informacion.st_mtime))
                #Crear un array para crear la fila con los items
                row = [name, date, type, size]
                #insertar la fila
                self.directorio.insertTopLevelItems(0, [QTreeWidgetItem(self.directorio, row)])
    
    #metodo que abre elemento al hacer dobleclick
    def openElement(self):
        #Obtener el item seleccionado por el usuario
        item = self.directorio.currentItem()
        #crear la ruta accediendo al nombre del elemento (carpeta o archivo)
        elemento = self.ruta.text() + "\\" + item.text(0)
        #si es un directorio navegar a su interior
        if path.isdir(elemento):
            self.ruta.setText(elemento)
            self.getDir()
        else: #si es un archivo abrirlo con el programa que lo abre por defecto en windows
            startfile(elemento)



app = QApplication(sys.argv)
dialogo = Dialogo()  #objeto de clase Dialogo
dialogo.show()
app.exec_()