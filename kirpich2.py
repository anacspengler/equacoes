# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kirpich2.ui'
#
# Created: Wed Aug  5 23:53:29 2015
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

class Ui_Kirpich2(object):
    def setupUi(self, Kirpich2):
        Kirpich2.setObjectName(_fromUtf8("Kirpich2"))
        Kirpich2.resize(400, 320)
        self.label = QtGui.QLabel(Kirpich2)
        self.label.setGeometry(QtCore.QRect(50, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Kirpich2)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 21, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Kirpich2)
        self.label_4.setGeometry(QtCore.QRect(190, 210, 21, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.resultado = QtGui.QLineEdit(Kirpich2)
        self.resultado.setGeometry(QtCore.QRect(190, 270, 161, 27))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.label_5 = QtGui.QLabel(Kirpich2)
        self.label_5.setGeometry(QtCore.QRect(190, 230, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Lt = QtGui.QDoubleSpinBox(Kirpich2)
        self.Lt.setGeometry(QtCore.QRect(80, 210, 91, 27))
        self.Lt.setObjectName(_fromUtf8("Lt"))
        self.St = QtGui.QDoubleSpinBox(Kirpich2)
        self.St.setGeometry(QtCore.QRect(230, 210, 91, 27))
        self.St.setObjectName(_fromUtf8("St"))
        self.calcular = QtGui.QPushButton(Kirpich2)
        self.calcular.setGeometry(QtCore.QRect(40, 270, 98, 27))
        self.calcular.setObjectName(_fromUtf8("calcular"))

        self.retranslateUi(Kirpich2)
        QtCore.QMetaObject.connectSlotsByName(Kirpich2)

    def retranslateUi(self, Kirpich2):
        Kirpich2.setWindowTitle(_translate("Kirpich2", "Kirpich II ", None))
        self.label.setText(_translate("Kirpich2", "Kirpich II ", None))
        self.label_3.setText(_translate("Kirpich2", "Lt:", None))
        self.label_4.setText(_translate("Kirpich2", "St:", None))
        self.label_5.setText(_translate("Kirpich2", "Tempo de concentracao: ", None))
        self.calcular.setText(_translate("Kirpich2", "Calcular", None))

