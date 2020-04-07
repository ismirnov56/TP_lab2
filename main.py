# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMessageBox
from gui import Ui_MainWindow

import sys

from createXML import create_xml
from cyclists import Cyclist
import downloadXML

class MainWindow(QtWidgets.QMainWindow):

    cyclist1 = Cyclist()
    cyclist2 = Cyclist()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBoxC1.addItem("Right")
        self.ui.comboBoxC1.addItem("Left")

        self.ui.comboBoxC2.addItem("Right")
        self.ui.comboBoxC2.addItem("Left")

        try:
            downloadXML.download(self.cyclist1, self.cyclist2)
        except Exception:
            print("Пустота")
        self.ui.c1_x.setValue(self.cyclist1.getCoordinate())
        self.ui.c1_v.setValue(self.cyclist1.getSpeed())
        self.ui.c2_x.setValue(self.cyclist2.getCoordinate())
        self.ui.c2_v.setValue(self.cyclist2.getSpeed())
        self.ui.pushButtonOk.clicked.connect(self.btnClickOk)


    def btnClickOk(self):
        self.cyclist1.setCoordinate(self.ui.c1_x.value())
        self.cyclist1.setSpeed(self.ui.c1_v.value())
        self.cyclist2.setCoordinate(self.ui.c2_x.value())
        self.cyclist2.setSpeed(self.ui.c2_v.value())
        self.cyclist1.setNewXinTime(self.ui.time.value(), self.ui.comboBoxC1.currentIndex())
        self.cyclist2.setNewXinTime(self.ui.time.value(), self.ui.comboBoxC2.currentIndex())
        self.ui.result.setText("Расстояние между велосипедистами " + str(abs(self.cyclist1.getCoordinate() - self.cyclist2.getCoordinate())))
        self.ui.c1_x.setValue(self.cyclist1.getCoordinate())
        self.ui.c2_x.setValue(self.cyclist2.getCoordinate())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Выход", "вы действительно хотите выйти?",
                QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            create_xml(self.cyclist1, self.cyclist2)
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())