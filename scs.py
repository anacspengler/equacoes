# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scs.ui'
#
# Created: Thu Oct  1 17:50:22 2015
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
        Scs.resize(570, 687)
        Scs.setMinimumSize(QtCore.QSize(0, 0))
        self.label = QtGui.QLabel(Scs)
        self.label.setGeometry(QtCore.QRect(10, 310, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Scs)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 51, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Scs)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Scs)
        self.label_4.setGeometry(QtCore.QRect(490, 260, 51, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scs = QtGui.QPushButton(Scs)
        self.scs.setGeometry(QtCore.QRect(440, 650, 98, 27))
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
        self.area4 = QtGui.QDoubleSpinBox(Scs)
        self.area4.setGeometry(QtCore.QRect(90, 400, 62, 27))
        self.area4.setObjectName(_fromUtf8("area4"))
        self.label_6 = QtGui.QLabel(Scs)
        self.label_6.setGeometry(QtCore.QRect(10, 400, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.area5 = QtGui.QDoubleSpinBox(Scs)
        self.area5.setGeometry(QtCore.QRect(90, 430, 62, 27))
        self.area5.setObjectName(_fromUtf8("area5"))
        self.area6 = QtGui.QDoubleSpinBox(Scs)
        self.area6.setGeometry(QtCore.QRect(90, 460, 62, 27))
        self.area6.setObjectName(_fromUtf8("area6"))
        self.label_7 = QtGui.QLabel(Scs)
        self.label_7.setGeometry(QtCore.QRect(10, 430, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(Scs)
        self.label_9.setGeometry(QtCore.QRect(10, 460, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Scs)
        self.label_10.setGeometry(QtCore.QRect(10, 580, 66, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_12 = QtGui.QLabel(Scs)
        self.label_12.setGeometry(QtCore.QRect(10, 520, 66, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.area10 = QtGui.QDoubleSpinBox(Scs)
        self.area10.setGeometry(QtCore.QRect(90, 580, 62, 27))
        self.area10.setObjectName(_fromUtf8("area10"))
        self.label_13 = QtGui.QLabel(Scs)
        self.label_13.setGeometry(QtCore.QRect(10, 490, 66, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.area8 = QtGui.QDoubleSpinBox(Scs)
        self.area8.setGeometry(QtCore.QRect(90, 520, 62, 27))
        self.area8.setObjectName(_fromUtf8("area8"))
        self.label_14 = QtGui.QLabel(Scs)
        self.label_14.setGeometry(QtCore.QRect(10, 550, 66, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.area7 = QtGui.QDoubleSpinBox(Scs)
        self.area7.setGeometry(QtCore.QRect(90, 490, 62, 27))
        self.area7.setObjectName(_fromUtf8("area7"))
        self.area9 = QtGui.QDoubleSpinBox(Scs)
        self.area9.setGeometry(QtCore.QRect(90, 550, 62, 27))
        self.area9.setObjectName(_fromUtf8("area9"))
        self.label_11 = QtGui.QLabel(Scs)
        self.label_11.setGeometry(QtCore.QRect(10, 610, 71, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.areaTotal = QtGui.QLineEdit(Scs)
        self.areaTotal.setGeometry(QtCore.QRect(90, 610, 61, 27))
        self.areaTotal.setObjectName(_fromUtf8("areaTotal"))
        self.cn5 = QtGui.QDoubleSpinBox(Scs)
        self.cn5.setGeometry(QtCore.QRect(180, 430, 62, 27))
        self.cn5.setObjectName(_fromUtf8("cn5"))
        self.cn6 = QtGui.QDoubleSpinBox(Scs)
        self.cn6.setGeometry(QtCore.QRect(180, 460, 62, 27))
        self.cn6.setObjectName(_fromUtf8("cn6"))
        self.cn4 = QtGui.QDoubleSpinBox(Scs)
        self.cn4.setGeometry(QtCore.QRect(180, 400, 62, 27))
        self.cn4.setObjectName(_fromUtf8("cn4"))
        self.cn8 = QtGui.QDoubleSpinBox(Scs)
        self.cn8.setGeometry(QtCore.QRect(180, 520, 62, 27))
        self.cn8.setObjectName(_fromUtf8("cn8"))
        self.cn9 = QtGui.QDoubleSpinBox(Scs)
        self.cn9.setGeometry(QtCore.QRect(180, 550, 62, 27))
        self.cn9.setObjectName(_fromUtf8("cn9"))
        self.cn7 = QtGui.QDoubleSpinBox(Scs)
        self.cn7.setGeometry(QtCore.QRect(180, 490, 62, 27))
        self.cn7.setObjectName(_fromUtf8("cn7"))
        self.cn10 = QtGui.QDoubleSpinBox(Scs)
        self.cn10.setGeometry(QtCore.QRect(180, 580, 62, 27))
        self.cn10.setObjectName(_fromUtf8("cn10"))
        self.label_15 = QtGui.QLabel(Scs)
        self.label_15.setGeometry(QtCore.QRect(0, 270, 91, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.precipitacao = QtGui.QLineEdit(Scs)
        self.precipitacao.setGeometry(QtCore.QRect(90, 270, 81, 27))
        self.precipitacao.setObjectName(_fromUtf8("precipitacao"))
        self.cnMedio = QtGui.QLineEdit(Scs)
        self.cnMedio.setGeometry(QtCore.QRect(180, 610, 61, 27))
        self.cnMedio.setObjectName(_fromUtf8("cnMedio"))
        self.label_5 = QtGui.QLabel(Scs)
        self.label_5.setGeometry(QtCore.QRect(270, 280, 31, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.sTotal = QtGui.QLineEdit(Scs)
        self.sTotal.setGeometry(QtCore.QRect(260, 610, 61, 27))
        self.sTotal.setObjectName(_fromUtf8("sTotal"))
        self.s1 = QtGui.QLineEdit(Scs)
        self.s1.setGeometry(QtCore.QRect(260, 310, 61, 27))
        self.s1.setObjectName(_fromUtf8("s1"))
        self.s2 = QtGui.QLineEdit(Scs)
        self.s2.setGeometry(QtCore.QRect(260, 340, 61, 27))
        self.s2.setObjectName(_fromUtf8("s2"))
        self.s3 = QtGui.QLineEdit(Scs)
        self.s3.setGeometry(QtCore.QRect(260, 370, 61, 27))
        self.s3.setObjectName(_fromUtf8("s3"))
        self.s8 = QtGui.QLineEdit(Scs)
        self.s8.setGeometry(QtCore.QRect(260, 520, 61, 27))
        self.s8.setObjectName(_fromUtf8("s8"))
        self.s7 = QtGui.QLineEdit(Scs)
        self.s7.setGeometry(QtCore.QRect(260, 490, 61, 27))
        self.s7.setObjectName(_fromUtf8("s7"))
        self.s6 = QtGui.QLineEdit(Scs)
        self.s6.setGeometry(QtCore.QRect(260, 460, 61, 27))
        self.s6.setObjectName(_fromUtf8("s6"))
        self.s5 = QtGui.QLineEdit(Scs)
        self.s5.setGeometry(QtCore.QRect(260, 430, 61, 27))
        self.s5.setObjectName(_fromUtf8("s5"))
        self.s4 = QtGui.QLineEdit(Scs)
        self.s4.setGeometry(QtCore.QRect(260, 400, 61, 27))
        self.s4.setObjectName(_fromUtf8("s4"))
        self.s10 = QtGui.QLineEdit(Scs)
        self.s10.setGeometry(QtCore.QRect(260, 580, 61, 27))
        self.s10.setObjectName(_fromUtf8("s10"))
        self.s9 = QtGui.QLineEdit(Scs)
        self.s9.setGeometry(QtCore.QRect(260, 550, 61, 27))
        self.s9.setObjectName(_fromUtf8("s9"))
        self.e9 = QtGui.QLineEdit(Scs)
        self.e9.setGeometry(QtCore.QRect(410, 550, 61, 27))
        self.e9.setObjectName(_fromUtf8("e9"))
        self.eTotal = QtGui.QLineEdit(Scs)
        self.eTotal.setGeometry(QtCore.QRect(410, 610, 61, 27))
        self.eTotal.setObjectName(_fromUtf8("eTotal"))
        self.e4 = QtGui.QLineEdit(Scs)
        self.e4.setGeometry(QtCore.QRect(410, 400, 61, 27))
        self.e4.setObjectName(_fromUtf8("e4"))
        self.e8 = QtGui.QLineEdit(Scs)
        self.e8.setGeometry(QtCore.QRect(410, 520, 61, 27))
        self.e8.setObjectName(_fromUtf8("e8"))
        self.e10 = QtGui.QLineEdit(Scs)
        self.e10.setGeometry(QtCore.QRect(410, 580, 61, 27))
        self.e10.setObjectName(_fromUtf8("e10"))
        self.e6 = QtGui.QLineEdit(Scs)
        self.e6.setGeometry(QtCore.QRect(410, 460, 61, 27))
        self.e6.setObjectName(_fromUtf8("e6"))
        self.e7 = QtGui.QLineEdit(Scs)
        self.e7.setGeometry(QtCore.QRect(410, 490, 61, 27))
        self.e7.setObjectName(_fromUtf8("e7"))
        self.e2 = QtGui.QLineEdit(Scs)
        self.e2.setGeometry(QtCore.QRect(410, 340, 61, 27))
        self.e2.setObjectName(_fromUtf8("e2"))
        self.e5 = QtGui.QLineEdit(Scs)
        self.e5.setGeometry(QtCore.QRect(410, 430, 61, 27))
        self.e5.setObjectName(_fromUtf8("e5"))
        self.e1 = QtGui.QLineEdit(Scs)
        self.e1.setGeometry(QtCore.QRect(410, 310, 61, 27))
        self.e1.setObjectName(_fromUtf8("e1"))
        self.e3 = QtGui.QLineEdit(Scs)
        self.e3.setGeometry(QtCore.QRect(410, 370, 61, 27))
        self.e3.setObjectName(_fromUtf8("e3"))
        self.v9 = QtGui.QLineEdit(Scs)
        self.v9.setGeometry(QtCore.QRect(480, 550, 61, 27))
        self.v9.setObjectName(_fromUtf8("v9"))
        self.v7 = QtGui.QLineEdit(Scs)
        self.v7.setGeometry(QtCore.QRect(480, 490, 61, 27))
        self.v7.setObjectName(_fromUtf8("v7"))
        self.v10 = QtGui.QLineEdit(Scs)
        self.v10.setGeometry(QtCore.QRect(480, 580, 61, 27))
        self.v10.setObjectName(_fromUtf8("v10"))
        self.v6 = QtGui.QLineEdit(Scs)
        self.v6.setGeometry(QtCore.QRect(480, 460, 61, 27))
        self.v6.setObjectName(_fromUtf8("v6"))
        self.v1 = QtGui.QLineEdit(Scs)
        self.v1.setGeometry(QtCore.QRect(480, 310, 61, 27))
        self.v1.setObjectName(_fromUtf8("v1"))
        self.v3 = QtGui.QLineEdit(Scs)
        self.v3.setGeometry(QtCore.QRect(480, 370, 61, 27))
        self.v3.setObjectName(_fromUtf8("v3"))
        self.v5 = QtGui.QLineEdit(Scs)
        self.v5.setGeometry(QtCore.QRect(480, 430, 61, 27))
        self.v5.setObjectName(_fromUtf8("v5"))
        self.v8 = QtGui.QLineEdit(Scs)
        self.v8.setGeometry(QtCore.QRect(480, 520, 61, 27))
        self.v8.setObjectName(_fromUtf8("v8"))
        self.v4 = QtGui.QLineEdit(Scs)
        self.v4.setGeometry(QtCore.QRect(480, 400, 61, 27))
        self.v4.setObjectName(_fromUtf8("v4"))
        self.v2 = QtGui.QLineEdit(Scs)
        self.v2.setGeometry(QtCore.QRect(480, 340, 61, 27))
        self.v2.setObjectName(_fromUtf8("v2"))
        self.vTotal = QtGui.QLineEdit(Scs)
        self.vTotal.setGeometry(QtCore.QRect(480, 610, 61, 27))
        self.vTotal.setObjectName(_fromUtf8("vTotal"))
        self.label_17 = QtGui.QLabel(Scs)
        self.label_17.setGeometry(QtCore.QRect(400, 250, 71, 51))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.ia2 = QtGui.QLineEdit(Scs)
        self.ia2.setGeometry(QtCore.QRect(340, 340, 61, 27))
        self.ia2.setObjectName(_fromUtf8("ia2"))
        self.ia9 = QtGui.QLineEdit(Scs)
        self.ia9.setGeometry(QtCore.QRect(340, 550, 61, 27))
        self.ia9.setObjectName(_fromUtf8("ia9"))
        self.iaTotal = QtGui.QLineEdit(Scs)
        self.iaTotal.setGeometry(QtCore.QRect(340, 610, 61, 27))
        self.iaTotal.setObjectName(_fromUtf8("iaTotal"))
        self.ia4 = QtGui.QLineEdit(Scs)
        self.ia4.setGeometry(QtCore.QRect(340, 400, 61, 27))
        self.ia4.setObjectName(_fromUtf8("ia4"))
        self.ia8 = QtGui.QLineEdit(Scs)
        self.ia8.setGeometry(QtCore.QRect(340, 520, 61, 27))
        self.ia8.setObjectName(_fromUtf8("ia8"))
        self.ia10 = QtGui.QLineEdit(Scs)
        self.ia10.setGeometry(QtCore.QRect(340, 580, 61, 27))
        self.ia10.setObjectName(_fromUtf8("ia10"))
        self.ia1 = QtGui.QLineEdit(Scs)
        self.ia1.setGeometry(QtCore.QRect(340, 310, 61, 27))
        self.ia1.setObjectName(_fromUtf8("ia1"))
        self.ia6 = QtGui.QLineEdit(Scs)
        self.ia6.setGeometry(QtCore.QRect(340, 460, 61, 27))
        self.ia6.setObjectName(_fromUtf8("ia6"))
        self.label_16 = QtGui.QLabel(Scs)
        self.label_16.setGeometry(QtCore.QRect(350, 280, 31, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.ia7 = QtGui.QLineEdit(Scs)
        self.ia7.setGeometry(QtCore.QRect(340, 490, 61, 27))
        self.ia7.setObjectName(_fromUtf8("ia7"))
        self.ia5 = QtGui.QLineEdit(Scs)
        self.ia5.setGeometry(QtCore.QRect(340, 430, 61, 27))
        self.ia5.setObjectName(_fromUtf8("ia5"))
        self.ia3 = QtGui.QLineEdit(Scs)
        self.ia3.setGeometry(QtCore.QRect(340, 370, 61, 27))
        self.ia3.setObjectName(_fromUtf8("ia3"))

        self.retranslateUi(Scs)
        QtCore.QMetaObject.connectSlotsByName(Scs)

    def retranslateUi(self, Scs):
        Scs.setWindowTitle(_translate("Scs", "SCS", None))
        self.label.setText(_translate("Scs", "Area I:", None))
        self.label_2.setText(_translate("Scs", "Area II:", None))
        self.label_3.setText(_translate("Scs", "Area III:", None))
        self.label_4.setText(_translate("Scs", "Volume\n"
"  (m3):", None))
        self.scs.setText(_translate("Scs", "SCS", None))
        self.label_8.setText(_translate("Scs", "CN:", None))
        self.label_6.setText(_translate("Scs", "Area IV:", None))
        self.label_7.setText(_translate("Scs", "Area V:", None))
        self.label_9.setText(_translate("Scs", "Area VI:", None))
        self.label_10.setText(_translate("Scs", "Area X:", None))
        self.label_12.setText(_translate("Scs", "Area VIII:", None))
        self.label_13.setText(_translate("Scs", "Area VII:", None))
        self.label_14.setText(_translate("Scs", "Area IX:", None))
        self.label_11.setText(_translate("Scs", "Total:", None))
        self.label_15.setText(_translate("Scs", "Precipitacao:", None))
        self.label_5.setText(_translate("Scs", "S:", None))
        self.label_17.setText(_translate("Scs", "    Chuva\n"
"Excedente\n"
"    (mm):", None))
        self.label_16.setText(_translate("Scs", "Ia:", None))

