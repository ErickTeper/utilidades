import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5 import uic

class Navegador(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("treewidget.ui", self)
        #url por defecto
        default_url = "http://www.google.com"
        #navegador a la url por defecto
        self.navegador.serUrl(QUrl(default_url))
        #agregar al buscador la url por defecto
        self.url.setText(default_url)
        #Desactivar boton back hasta que no haya historial
        self.btn_back.setEnable(False)
        #retroceder a la pagina anteriosr
        self.bton_back.clicked.connect(self.navegador.back)
        self.url.returnPressed.connect(self.navegar)
        self.navegador.urlChanged.connect(self.url_changed)

    # navegar a la url indicada en al buscador al pulsar enter
    def navegar(self):
        url = QUrl(self.url.text())
        self.navegador.setUrl(url)

    #Detectar el cambio de url de la navegacion
    def url_changed(self):
        #crear un objeto de la pagina para accede al historial
    page = self.navegador.page()
    history = page.history()
    #si hay historial activar el boton back
    if history.canGoBack()
        self.bot_back.setEnabled(True)
    else:
        self.btn_back.setEnable(False)
    #agregar el cambio de url al campo de busqueda
    url = self.naveggador.url()
    self.url.setText(url.toString())





app = QApplication(sys.argv)
navegador = Navegador()  #objeto de clase navegador
navegador.show()
app.exec_()