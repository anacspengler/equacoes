# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scs.ui'
#
# Created: Wed Aug 12 23:06:31 2015
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

class Ui_Scs(object):
    def setupUi(self, Scs):
        Scs.setObjectName(_fromUtf8("Scs"))
        Scs.resize(460, 454)
        Scs.setMinimumSize(QtCore.QSize(0, 0))
        self.label = QtGui.QLabel(Scs)
        self.label.setGeometry(QtCore.QRect(20, 320, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Scs)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Scs)
        self.label_3.setGeometry(QtCore.QRect(20, 380, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Scs)
        self.label_4.setGeometry(QtCore.QRect(250, 420, 61, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.volume = QtGui.QLineEdit(Scs)
        self.volume.setGeometry(QtCore.QRect(310, 420, 113, 27))
        self.volume.setToolTip(_fromUtf8(""))
        self.volume.setStatusTip(_fromUtf8(""))
        self.volume.setWhatsThis(_fromUtf8(""))
        self.volume.setAutoFillBackground(True)
        self.volume.setObjectName(_fromUtf8("volume"))
        self.scs = QtGui.QPushButton(Scs)
        self.scs.setGeometry(QtCore.QRect(20, 420, 98, 27))
        self.scs.setObjectName(_fromUtf8("scs"))
        self.cn1 = QtGui.QDoubleSpinBox(Scs)
        self.cn1.setGeometry(QtCore.QRect(180, 310, 62, 27))
        self.cn1.setObjectName(_fromUtf8("cn1"))
        self.label_8 = QtGui.QLabel(Scs)
        self.label_8.setGeometry(QtCore.QRect(190, 280, 31, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cn2 = QtGui.QDoubleSpinBox(Scs)
        self.cn2.setGeometry(QtCore.QRect(180, 340, 62, 27))
        self.cn2.setObjectName(_fromUtf8("cn2"))
        self.cn3 = QtGui.QDoubleSpinBox(Scs)
        self.cn3.setGeometry(QtCore.QRect(180, 370, 62, 27))
        self.cn3.setObjectName(_fromUtf8("cn3"))
        self.area3 = QtGui.QDoubleSpinBox(Scs)
        self.area3.setGeometry(QtCore.QRect(90, 370, 62, 27))
        self.area3.setObjectName(_fromUtf8("area3"))
        self.area1 = QtGui.QDoubleSpinBox(Scs)
        self.area1.setGeometry(QtCore.QRect(90, 310, 62, 27))
        self.area1.setObjectName(_fromUtf8("area1"))
        self.area2 = QtGui.QDoubleSpinBox(Scs)
        self.area2.setGeometry(QtCore.QRect(90, 340, 62, 27))
        self.area2.setObjectName(_fromUtf8("area2"))
        self.label_5 = QtGui.QLabel(Scs)
        self.label_5.setGeometry(QtCore.QRect(270, 277, 41, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tipo1 = QtGui.QSpinBox(Scs)
        self.tipo1.setGeometry(QtCore.QRect(270, 310, 60, 27))
        self.tipo1.setObjectName(_fromUtf8("tipo1"))
        self.tipo2 = QtGui.QSpinBox(Scs)
        self.tipo2.setGeometry(QtCore.QRect(270, 340, 60, 27))
        self.tipo2.setObjectName(_fromUtf8("tipo2"))
        self.tipo3 = QtGui.QSpinBox(Scs)
        self.tipo3.setGeometry(QtCore.QRect(270, 370, 60, 27))
        self.tipo3.setObjectName(_fromUtf8("tipo3"))

        self.retranslateUi(Scs)
        QtCore.QMetaObject.connectSlotsByName(Scs)

    def retranslateUi(self, Scs):
        Scs.setWindowTitle(_translate("Scs", "SCS", None))
        self.label.setText(_translate("Scs", "Area I:", None))
        self.label_2.setText(_translate("Scs", "Area II:", None))
        self.label_3.setText(_translate("Scs", "Area III:", None))
        self.label_4.setText(_translate("Scs", "Volume:", None))
        self.scs.setText(_translate("Scs", "SCS", None))
        self.label_8.setText(_translate("Scs", "CN:", None))
        self.label_5.setText(_translate("Scs", "Tipo:", None))

