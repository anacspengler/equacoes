# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bransby.ui'
#
# Created: Wed Aug  5 23:56:20 2015
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

class Ui_Bransby(object):
    def setupUi(self, Bransby):
        Bransby.setObjectName(_fromUtf8("Bransby"))
        Bransby.resize(400, 320)
        self.resultado = QtGui.QLineEdit(Bransby)
        self.resultado.setGeometry(QtCore.QRect(190, 270, 171, 27))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.label_2 = QtGui.QLabel(Bransby)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.calcular = QtGui.QPushButton(Bransby)
        self.calcular.setGeometry(QtCore.QRect(40, 270, 98, 27))
        self.calcular.setObjectName(_fromUtf8("calcular"))
        self.label_4 = QtGui.QLabel(Bransby)
        self.label_4.setGeometry(QtCore.QRect(140, 200, 21, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(Bransby)
        self.label_6.setGeometry(QtCore.QRect(190, 230, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_3 = QtGui.QLabel(Bransby)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 21, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.St = QtGui.QDoubleSpinBox(Bransby)
        self.St.setGeometry(QtCore.QRect(170, 200, 91, 27))
        self.St.setObjectName(_fromUtf8("St"))
        self.label = QtGui.QLabel(Bransby)
        self.label.setGeometry(QtCore.QRect(270, 200, 16, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Lt = QtGui.QDoubleSpinBox(Bransby)
        self.Lt.setGeometry(QtCore.QRect(40, 200, 91, 27))
        self.Lt.setObjectName(_fromUtf8("Lt"))
        self.A = QtGui.QDoubleSpinBox(Bransby)
        self.A.setGeometry(QtCore.QRect(290, 200, 91, 27))
        self.A.setObjectName(_fromUtf8("A"))

        self.retranslateUi(Bransby)
        QtCore.QMetaObject.connectSlotsByName(Bransby)

    def retranslateUi(self, Bransby):
        Bransby.setWindowTitle(_translate("Bransby", "Bransby - Willians", None))
        self.label_2.setText(_translate("Bransby", "Bransby - Willians", None))
        self.calcular.setText(_translate("Bransby", "Calcular", None))
        self.label_4.setText(_translate("Bransby", "St:", None))
        self.label_6.setText(_translate("Bransby", "Tempo de concentracao: ", None))
        self.label_3.setText(_translate("Bransby", "Lt:", None))
        self.label.setText(_translate("Bransby", "A:", None))

