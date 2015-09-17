#ARQUIVO DE CODIGO Q NAO EH DO UI

import sys 
from PyQt4 import QtGui, QtCore

from scs import Ui_Scs

class Scs(QtGui.QWidget, Ui_Scs):
	def __init__(self, precipitacao, parent=None):
		super(Scs, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		precipitacao = self.precipitacao
		
		self.scs.clicked.connect(self.Calcula)

	def Calcula(self):	
		
		a1 = self.area1.value()
		a2 = self.area2.value()
		a3 = self.area3.value()
		a4 = self.area4.value()
		a5 = self.area5.value()
		a6 = self.area6.value()
		a7 = self.area7.value()
		a8 = self.area8.value()
		a9 = self.area9.value()
		a10 = self.area10.value()

		#cn da area 1
		cn1 = self.cn1.value()
		cn2 = self.cn2.value()
		cn3 = self.cn3.value()
		cn4 = self.cn4.value()
		cn5 = self.cn5.value()
		cn6 = self.cn6.value()
		cn7 = self.cn7.value()
		cn8 = self.cn8.value()
		cn9 = self.cn9.value()
		cn10 = self.cn10.value()
	
		#tipo da area 1
		#tipo1 = self.tipo1.value()
		#tipo2 = self.tipo2.value()
		#tipo3 = self.tipo3.value()
		
		#if(tipo1 == 1):
		#	cnValido1 = (cn1 * 10) / (4.2 + (0.058 * cn1))
		#if(tipo1 == 3):
		#	cnValido1 = (cn1 * 10) / (23 - (0.13 * cn1))
		#else:
		#	cnValido1 = cn1 
			
		#if(tipo2 == 1):
		#	cnValido2 = (cn2 * 10) / (4.2 + (0.058 * cn2))
		#if(tipo2 == 3):
		#	cnValido2 = (cn2 * 10) / (23 - (0.13 * cn2))
		#else:
		#	cnValido2 = cn2		
				
		#if(tipo3 == 1):
		#	cnValido3 = (cn3 * 10) / (4.2 + (0.058 * cn3))
		#if(tipo3 == 3):
		#	cnValido3 = (cn3 * 10) / (23 - (0.13 * cn3))
		#else:
		#	cnValido3 = cn3	
		
		areaTotal = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
		self.areaTotal.setText(str(areaTotal))
				
		#cnMedio = ((a1 * cnValido1) + (a2 * cnValido2) + (a3 * cnValido3)) / areaTotal
		
		cnMedio = ((a1*cn1)+(a2*cn2)+(a3*cn3)+(a4*cn4)+(a5*cn5)+(a6*cn6)+(a7*cn7)+(a8*cn8)+(a9*cn9)+(a10*cn10)) / areaTotal
		self.cnMedio.setText(str(cnMedio))
		
		s1 = ((1000 / cn1) - 10) * 25.4
		s2 = ((1000 / cn2) - 10) * 25.4
		s3 = ((1000 / cn3) - 10) * 25.4
		s4 = ((1000 / cn4) - 10) * 25.4
		s5 = ((1000 / cn5) - 10) * 25.4
		s6 = ((1000 / cn6) - 10) * 25.4
		s7 = ((1000 / cn7) - 10) * 25.4
		s8 = ((1000 / cn8) - 10) * 25.4
		s9 = ((1000 / cn9) - 10) * 25.4
		s10 = ((1000 / cn10) - 10) * 25.4
		
		sTotal = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10/10
		
		self.s1.setText(str(s1))
		self.s2.setText(str(s2))
		self.s3.setText(str(s3))
		self.s4.setText(str(s4))
		self.s5.setText(str(s5))
		self.s6.setText(str(s6))
		self.s7.setText(str(s7))
		self.s8.setText(str(s8))
		self.s9.setText(str(s9))
		self.s10.setText(str(s10))
		self.sTotal.setText(str(sTotal))
		
		ia1 = s1 * 0.2
		ia2 = s2 * 0.2
		ia3 = s3 * 0.2
		ia4 = s4 * 0.2
		ia5 = s5 * 0.2
		ia6 = s6 * 0.2
		ia7 = s7 * 0.2
		ia8 = s8 * 0.2
		ia9 = s9 * 0.2
		ia10 = s10 * 0.2
		
		iaTotal = ia1 + ia2 + ia3 + ia4 + ia5 + ia6 + ia7 + ia8 + ia9 +ia10/10
		
		self.ia1.setText(str(ia1))
		self.ia2.setText(str(ia2))
		self.ia3.setText(str(ia3))
		self.ia4.setText(str(ia4))
		self.ia5.setText(str(ia5))
		self.ia6.setText(str(ia6))
		self.ia7.setText(str(ia7))
		self.ia8.setText(str(ia8))
		self.ia9.setText(str(ia9))
		self.ia10.setText(str(ia10))
		self.iaTotal.setText(str(iaTotal))
		
		#VER ISSO 
		if(precipitacao > ia1):
			e1 = (precipitacao - ia1) / (precipitacao - ia1 + s1)
		else:
			e1 = 0 
		if(precipitacao > ia2):
			e2 = (precipitacao - ia2) / (precipitacao - ia2 + s2)
		else:
			e2 = 0 
		if(precipitacao > ia3):
			e3 = (precipitacao - ia3) / (precipitacao - ia3 + s3)
		else:
			e3 = 0 
		if(precipitacao > ia4):
			e4 = (precipitacao - ia4) / (precipitacao - ia4 + s4)
		else:
			e4 = 0 
		if(precipitacao > ia5):
			e5 = (precipitacao - ia5) / (precipitacao - ia5 + s5)
		else:
			e5 = 0 
		if(precipitacao > ia6):
			e6 = (precipitacao - ia6) / (precipitacao - ia7 + s7)
		else:
			e6 = 0 
		if(precipitacao > ia7):
			e7 = (precipitacao - ia7) / (precipitacao - ia7 + s7)
		else:
			e7 = 0 
		if(precipitacao > ia8):
			e8 = (precipitacao - ia8) / (precipitacao - ia8 + s8)
		else:
			e8 = 0 
		if(precipitacao > ia9):
			e9 = (precipitacao - ia9) / (precipitacao - ia9 + s9)
		else:
			e9 = 0 
		if(precipitacao > ia10):
			e10 = (precipitacao - ia10) / (precipitacao - ia10 + s10)
		else:
			e10 = 0 
			
		eTotal = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10/10
		
		self.e1.setText(str(e1))
		self.e2.setText(str(e2))
		self.e3.setText(str(e3))
		self.e4.setText(str(e4))
		self.e5.setText(str(e5))
		self.e6.setText(str(e6))
		self.e7.setText(str(e7))
		self.e8.setText(str(e8))
		self.e9.setText(str(e9))
		self.e10.setText(str(e10))
		self.eTotal.setText(str(eTotal))
		
		v1 = (e1 * a1) / 1000
		v2 = (e2 * a2) / 1000
		v3 = (e3 * a3) / 1000
		v4 = (e4 * a4) / 1000
		v5 = (e5 * a5) / 1000
		v6 = (e6 * a6) / 1000
		v7 = (e7 * a7) / 1000
		v8 = (e8 * a8) / 1000
		v9 = (e9 * a9) / 1000
		v10 = (e10 * a10) / 1000
		
		vTotal = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
		
		self.v1.setText(str(v1))
		self.v2.setText(str(v2))
		self.v3.setText(str(v3))
		self.v4.setText(str(v4))
		self.v5.setText(str(v5))
		self.v6.setText(str(v6))
		self.v7.setText(str(v7))
		self.v8.setText(str(v8))
		self.v9.setText(str(v9))
		self.v10.setText(str(v10))
		self.vTotal.setText(str(vTotal))
		
		#essa parte de cima eh o q eu vou mostrar
		#coisas que so calcula escondida para gerar o hidrograma utitario
		
		#Precipitacao Unitaria em mm
		pUnitario = 1
		
		#Duracao Unitaria em min
		#Discretizacao q o usuario escolheu
		#N EH dez
		tu = 10
		#converter para h
		#tu = tu/60
		
		#Tempo de Concentracao em h
		#PUXAR DE EMPIRICAS
		#N EH 1
		tc = 1
		
		#Tempo de Pico em h
		ta = tu/2 + 0.6 * tc
		
		#Tempo de Base em h
		tb = 2.67 * ta
		
		#Vazao de Pico 
		vp = (0.75 * areaTotal * pUnitario)/(3.6 * ta)
		
		#Convertendo para minutos e arredondando
		#ver como arredonda
		ta = int((ta * 60))
		tb = int((tb * 60))
		
		#Arredondando
		vp = int(vp)
		
		#Para a reta Ascendente
		a1 = 0
		b1 = float(vp)/float(ta)
		
		#Para a reta Descendente
		b2 = float((-vp))/float((tb-ta))		
		a2 = float(-tb * b2)

		#lista q ira conter a discretizacao
		ldiscretizacao = []
		#variavel para a discretizacao
		aux = 0
		
		while(aux <= ta):
			ldiscretizacao.append(a1+(b1*aux))
			aux = aux + tu
			
		 while(aux <= tb):
			ldiscretizacao.append(a2+(b2*aux))
			aux = aux + tu
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
