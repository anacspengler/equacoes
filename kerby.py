# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kerby.ui'
#
# Created: Wed Aug  5 23:50:58 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Kerby(object):
    def setupUi(self, Kerby):
        Kerby.setObjectName(_fromUtf8("Kerby"))
        Kerby.resize(400, 320)
        self.label_5 = QtGui.QLabel(Kerby)
        self.label_5.setGeometry(QtCore.QRect(190, 230, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.resultado = QtGui.QLineEdit(Kerby)
        self.resultado.setGeometry(QtCore.QRect(190, 270, 171, 27))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.St = QtGui.QDoubleSpinBox(Kerby)
        self.St.setGeometry(QtCore.QRect(170, 200, 91, 27))
        self.St.setObjectName(_fromUtf8("St"))
        self.label_3 = QtGui.QLabel(Kerby)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 21, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Kerby)
        self.label_4.setGeometry(QtCore.QRect(140, 200, 21, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Lt = QtGui.QDoubleSpinBox(Kerby)
        self.Lt.setGeometry(QtCore.QRect(40, 200, 91, 27))
        self.Lt.setObjectName(_fromUtf8("Lt"))
        self.label = QtGui.QLabel(Kerby)
        self.label.setGeometry(QtCore.QRect(270, 200, 16, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.r = QtGui.QDoubleSpinBox(Kerby)
        self.r.setGeometry(QtCore.QRect(290, 200, 91, 27))
        self.r.setObjectName(_fromUtf8("r"))
        self.label_2 = QtGui.QLabel(Kerby)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.calcular = QtGui.QPushButton(Kerby)
        self.calcular.setGeometry(QtCore.QRect(30, 270, 98, 27))
        self.calcular.setObjectName(_fromUtf8("calcular"))

        self.retranslateUi(Kerby)
        QtCore.QMetaObject.connectSlotsByName(Kerby)

    def retranslateUi(self, Kerby):
        Kerby.setWindowTitle(_translate("Kerby", "Kerby", None))
        self.label_5.setText(_translate("Kerby", "Tempo de concentracao: ", None))
        self.label_3.setText(_translate("Kerby", "Lt:", None))
        self.label_4.setText(_translate("Kerby", "St:", None))
        self.label.setText(_translate("Kerby", "r:", None))
        self.label_2.setText(_translate("Kerby", "Kerby", None))
        self.calcular.setText(_translate("Kerby", "Calcular", None))

