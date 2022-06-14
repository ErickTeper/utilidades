import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("slider.ui", self)

        #horizontal slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.getValueHorizontal)

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setSingleStep(10)
        self.verticalSlider.setValue(250)
        self.verticalSlider.valueChanged.connect(self.getValueVertical)


    def getValueHorizontal(self):
        value = self.horizontalSlider.value()
        self.labelHorizontal.setText(str(value))

    def getValueVertical(self):
        value = self.verticalSlider.value()
        self.labelVertical.setText(str(value))






app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()