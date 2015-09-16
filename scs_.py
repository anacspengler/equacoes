#ARQUIVO DE CODIGO Q NAO EH DO UI

import sys 
from PyQt4 import QtGui, QtCore

from scs import Ui_Scs

class Scs(QtGui.QWidget, Ui_Scs):
	def __init__(self, lintensidade, lblocosAlternados, parent=None):
		super(Scs, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.lintensidade = lintensidade
		self.lblocosAlternados = lblocosAlternados
		
		self.scs.clicked.connect(self.Calcula)

	def Calcula(self):	
		
		a1 = self.area1.value()
		a2 = self.area2.value()
		a3 = self.area3.value()

		#cn da area 1
		cn1 = self.cn1.value()
		cn2 = self.cn2.value()
		cn3 = self.cn3.value()
		
		#tipo da area 1
		tipo1 = self.tipo1.value()
		tipo2 = self.tipo2.value()
		tipo3 = self.tipo3.value()
		
		if(tipo1 == 1):
			cnValido1 = (cn1 * 10) / (4.2 + (0.058 * cn1))
		if(tipo1 == 3):
			cnValido1 = (cn1 * 10) / (23 - (0.13 * cn1))
		else:
			cnValido1 = cn1 
			
		if(tipo2 == 1):
			cnValido2 = (cn2 * 10) / (4.2 + (0.058 * cn2))
		if(tipo2 == 3):
			cnValido2 = (cn2 * 10) / (23 - (0.13 * cn2))
		else:
			cnValido2 = cn2		
				
		if(tipo3 == 1):
			cnValido3 = (cn3 * 10) / (4.2 + (0.058 * cn3))
		if(tipo3 == 3):
			cnValido3 = (cn3 * 10) / (23 - (0.13 * cn3))
		else:
			cnValido3 = cn3	
				
		cnMedio = ((a1 * cnValido1) + (a2 * cnValido2) + (a3 * cnValido3)) / (a1 + a2 + a3)
		
		s = ((1000 / cnMedio) - 10) * 25.4
		
		#print(self.lblocosAlternados)
			
		lacumulada = []
		lacumulada.append(self.lblocosAlternados[0])
		i = 1
		
		while i < len(self.lblocosAlternados):
			lacumulada.append(self.lblocosAlternados[i] + lacumulada[i -1])
			i = i + 1
		
		print(lacumulada)	
		
		lexchuva = []
		i = 0
		while i < len(lacumulada):
			if(lacumulada[i] < (s * 0.2)):
				lexchuva.append(0)
			else:
				lexchuva.append((lacumulada[i] - (s * 0.2))**2/ (lacumulada[i] + (s * 0.8)))
			i = i + 1
		
		print("\n\n\n\n")
		print(s)
		print(lexchuva)
		
		i = 1
		lexecedente = []
		lexecedente.append(lexchuva[0])
		while i < len(lexchuva):
			lexecedente.append(lexchuva[i] - lexchuva[i-1])
			i = i + 1
		
		print("\n\n\n\n")
		print(lexecedente)
		
		volume = sum(lexecedente) * 1000
		
		self.volume.setText(str(volume))
