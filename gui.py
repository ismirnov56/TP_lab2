# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 1058)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 702, 1014))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(100, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.c1_x = QtWidgets.QDoubleSpinBox(self.widget)
        self.c1_x.setMinimumSize(QtCore.QSize(100, 30))
        self.c1_x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.c1_x.setMinimum(-4000000.0)
        self.c1_x.setMaximum(4000000.0)
        self.c1_x.setObjectName("c1_x")
        self.verticalLayout.addWidget(self.c1_x)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.c1_v = QtWidgets.QDoubleSpinBox(self.widget)
        self.c1_v.setMinimumSize(QtCore.QSize(100, 30))
        self.c1_v.setMaximumSize(QtCore.QSize(16777215, 30))
        self.c1_v.setMaximum(4000000.0)
        self.c1_v.setObjectName("c1_v")
        self.verticalLayout.addWidget(self.c1_v)
        self.comboBoxC1 = QtWidgets.QComboBox(self.widget)
        self.comboBoxC1.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxC1.setObjectName("comboBoxC1")
        self.verticalLayout.addWidget(self.comboBoxC1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.c2_x = QtWidgets.QDoubleSpinBox(self.widget)
        self.c2_x.setMinimumSize(QtCore.QSize(100, 30))
        self.c2_x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.c2_x.setMinimum(-4000000.0)
        self.c2_x.setMaximum(4000000.0)
        self.c2_x.setObjectName("c2_x")
        self.verticalLayout_2.addWidget(self.c2_x)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(100, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.c2_v = QtWidgets.QDoubleSpinBox(self.widget)
        self.c2_v.setMinimumSize(QtCore.QSize(100, 30))
        self.c2_v.setMaximumSize(QtCore.QSize(16777215, 30))
        self.c2_v.setMaximum(4000000.0)
        self.c2_v.setObjectName("c2_v")
        self.verticalLayout_2.addWidget(self.c2_v)
        self.comboBoxC2 = QtWidgets.QComboBox(self.widget)
        self.comboBoxC2.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxC2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBoxC2.setObjectName("comboBoxC2")
        self.verticalLayout_2.addWidget(self.comboBoxC2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(600, 600))
        self.widget1.setMaximumSize(QtCore.QSize(700, 700))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3.addWidget(self.widget1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(100, 30))
        self.label_7.setMaximumSize(QtCore.QSize(700, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.time = QtWidgets.QDoubleSpinBox(self.widget)
        self.time.setMinimumSize(QtCore.QSize(100, 30))
        self.time.setMaximumSize(QtCore.QSize(700, 30))
        self.time.setMaximum(4000000.0)
        self.time.setObjectName("time")
        self.horizontalLayout_2.addWidget(self.time)
        self.pushButtonOk = QtWidgets.QPushButton(self.widget)
        self.pushButtonOk.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButtonOk.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_2.addWidget(self.pushButtonOk)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.result = QtWidgets.QLabel(self.widget)
        self.result.setMinimumSize(QtCore.QSize(100, 40))
        self.result.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout_3.addWidget(self.result)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cyclist 1"))
        self.label_2.setText(_translate("MainWindow", "Coordinate"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.label_4.setText(_translate("MainWindow", "Cyclist 2"))
        self.label_5.setText(_translate("MainWindow", "Coordinate"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.pushButtonOk.setText(_translate("MainWindow", "Ok"))