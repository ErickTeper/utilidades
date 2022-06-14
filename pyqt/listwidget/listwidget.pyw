import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("listwidget.ui", self)
        self.boton.clicked.connect(self.getItem)
        #agregar nuevos item
        self.lenguajes.addItem("visual Basic")
        #eliminar un item
        self.deleteItem("Python")

    def deleteItem(self, label):
        #array para almacenar cada item objeto
        items = []
        # count() retorna el total de items de la lista
        for x in range(self.lenguajes.count()):
            item = self.lenguajes.item(x)
            items.append(item)
        #Array almacena el texto de cada item
        labels = [i.text() for i in items]
        #Recorrer item a item el array labels
        for x in range(len(labels)):
            #Si el item existe
            if labels[x] == label:
                #eliminar
                item = self.lenguajes.indexFromItem(self.lenguajes.item(x))
                self.lenguajes.model().removeRow(item.row())


    def getItem(self):
        items = self.lenguajes.selectedItems()
        #array para guardar los items seleccionados
        selected = []
        for x in range(len(items)):
            selected.append(self.lenguajes.selectedItems()[x].text())
        self.labelLenguajes.setText("seleccionados: " + "-".join(selected))


app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()