# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kirpich1.ui'
#
# Created: Wed Aug  5 23:24:54 2015
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

class Ui_Kirpich1(object):
    def setupUi(self, Kirpich1):
        Kirpich1.setObjectName(_fromUtf8("Kirpich1"))
        Kirpich1.resize(400, 320)
        self.label = QtGui.QLabel(Kirpich1)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Kirpich1)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 251, 21))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.resultado = QtGui.QLineEdit(Kirpich1)
        self.resultado.setGeometry(QtCore.QRect(190, 270, 171, 27))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.label_5 = QtGui.QLabel(Kirpich1)
        self.label_5.setGeometry(QtCore.QRect(190, 230, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(Kirpich1)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 16, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Kirpich1)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 16, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Lt = QtGui.QDoubleSpinBox(Kirpich1)
        self.Lt.setGeometry(QtCore.QRect(70, 210, 91, 27))
        self.Lt.setObjectName(_fromUtf8("Lt"))
        self.h = QtGui.QDoubleSpinBox(Kirpich1)
        self.h.setGeometry(QtCore.QRect(220, 210, 91, 27))
        self.h.setObjectName(_fromUtf8("h"))
        self.calcular = QtGui.QPushButton(Kirpich1)
        self.calcular.setGeometry(QtCore.QRect(30, 260, 98, 27))
        self.calcular.setObjectName(_fromUtf8("calcular"))

        self.retranslateUi(Kirpich1)
        QtCore.QMetaObject.connectSlotsByName(Kirpich1)

    def retranslateUi(self, Kirpich1):
        Kirpich1.setWindowTitle(_translate("Kirpich1", "Kirpich I", None))
        self.label.setText(_translate("Kirpich1", "Kirpich I ", None))
        self.label_5.setText(_translate("Kirpich1", "Tempo de concentracao: ", None))
        self.label_2.setText(_translate("Kirpich1", "Lt:", None))
        self.label_3.setText(_translate("Kirpich1", "h:", None))
        self.calcular.setText(_translate("Kirpich1", "Calcular", None))

