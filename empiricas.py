import sys 
from PyQt4 import QtGui, QtCore

from bransby import Ui_Bransby 
from kirpich1 import Ui_Kirpich1 
from kirpich2 import Ui_Kirpich2 
from kerby import Ui_Kerby 

class Kirpich1(QtGui.QWidget, Ui_Kirpich1):
	def __init__(self, parent=None):
		super(Kirpich1, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.calcular.clicked.connect(self.Calcula)

	def Calcula(self):	
		#lendo parametros 
		Lt = self.Lt.value()
		h = self.h.value()
		
		tc = 0.0196 * (((Lt**3)/ h)** 0.385)
		
		self.resultado.setText(str(tc))
		
class Kirpich2(QtGui.QWidget, Ui_Kirpich2):
	def __init__(self, parent=None):
		super(Kirpich2, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.calcular.clicked.connect(self.Calcula)

	def Calcula(self):	
		#lendo parametros 
		Lt = self.Lt.value()
		St = self.St.value()
		
		tc = 0.28 * (((Lt**2)/ St)** 0.385)
		
		self.resultado.setText(str(tc))	
		
class Kerby(QtGui.QWidget, Ui_Kerby):
	def __init__(self, parent=None):
		super(Kerby, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.calcular.clicked.connect(self.Calcula)

	def Calcula(self):	
		#lendo parametros 
		Lt = self.Lt.value()
		St = self.St.value()
		r = self.r.value()
		
		tc = 7.23 * (((Lt*r)/ (St**0.5))** 0.476)
		
		self.resultado.setText(str(tc))	
		
class Bransby(QtGui.QWidget, Ui_Bransby):
	def __init__(self, parent=None):
		super(Bransby, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.calcular.clicked.connect(self.Calcula)

	def Calcula(self):	
		#lendo parametros 
		Lt = self.Lt.value()
		St = self.St.value()
		A = self.A.value()
		
		tc = 306 * (Lt/5280) * (1/((A**0.1)*(St**0.2)))
		
		self.resultado.setText(str(tc))		

