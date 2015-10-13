#ARQUIVO DE CODIGO Q NAO EH DO UI

import sys 
from PyQt4 import QtGui, QtCore

from scs import Ui_Scs

class Scs(QtGui.QWidget, Ui_Scs):
	def __init__(self, precipitacao, parent=None):
		super(Scs, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		
		self.precipitacao = precipitacao
		
		self.scs.clicked.connect(self.Calcula)

	def Calcula(self):	
		
		#self.precipitacao.setText(str(self.precipitacao))
		
		la = []
		la.append(self.area1.value())
		la.append(self.area2.value())
		la.append(self.area3.value())
		la.append(self.area4.value())
		la.append(self.area5.value())
		la.append(self.area6.value())
		la.append(self.area7.value())
		la.append(self.area8.value())
		la.append(self.area9.value())
		la.append(self.area10.value())
		
		areaTotal = sum(la)
		self.areaTotal.setText(str(areaTotal))

		lcn = []
		lcn.append(self.cn1.value())
		lcn.append(self.cn2.value())
		lcn.append(self.cn3.value())
		lcn.append(self.cn4.value())
		lcn.append(self.cn5.value())
		lcn.append(self.cn6.value())
		lcn.append(self.cn7.value())
		lcn.append(self.cn8.value())
		lcn.append(self.cn9.value())
		lcn.append(self.cn10.value())
		
		soma = 0
		for i in range(0,10):
			soma = soma + (lcn[i] * la[i])
		
		cnMedio = soma/areaTotal
		self.cnMedio.setText(str(cnMedio))
		
		ls = []
		qtd = 0
		for i in range(0, 10):
			if(lcn[i] > 0):
				ls.append(((1000 / lcn[i]) - 10) * 25.4)
				qtd = qtd + 1
			else:
				ls.append(0.0)
	
		soma = sum(ls)
		sTotal = soma/qtd
		
		self.s1.setText(str(ls[0]))
		self.s2.setText(str(ls[1]))
		self.s3.setText(str(ls[2]))
		self.s4.setText(str(ls[3]))
		self.s5.setText(str(ls[4]))
		self.s6.setText(str(ls[5]))
		self.s7.setText(str(ls[6]))
		self.s8.setText(str(ls[7]))
		self.s9.setText(str(ls[8]))
		self.s10.setText(str(ls[9]))
		self.sTotal.setText(str(sTotal))
		
		lia = []
		for i in range(0, 10):
			lia.append(ls[i]*0.2)
	
		soma = sum(lia)
		iaTotal = soma/qtd
		
		self.ia1.setText(str(lia[0]))
		self.ia2.setText(str(lia[1]))
		self.ia3.setText(str(lia[2]))
		self.ia4.setText(str(lia[3]))
		self.ia5.setText(str(lia[4]))
		self.ia6.setText(str(lia[5]))
		self.ia7.setText(str(lia[6]))
		self.ia8.setText(str(lia[7]))
		self.ia9.setText(str(lia[8]))
		self.ia10.setText(str(lia[9]))
		self.iaTotal.setText(str(iaTotal))
		
		le = []
		for i in range(0,10):
			if(self.precipitacao > lia[i] and lia[i] > 0):
				le.append((self.precipitacao - lia[i])**2 / (self.precipitacao - lia[i] + ls[i]))
			else:
				le.append(0.0)
		
		soma = sum(le)	
		eTotal = soma/qtd
		
		self.e1.setText(str(le[0]))
		self.e2.setText(str(le[1]))
		self.e3.setText(str(le[2]))
		self.e4.setText(str(le[3]))
		self.e5.setText(str(le[4]))
		self.e6.setText(str(le[5]))
		self.e7.setText(str(le[6]))
		self.e8.setText(str(le[7]))
		self.e9.setText(str(le[8]))
		self.e10.setText(str(le[9]))
		self.eTotal.setText(str(eTotal))
		
		lv = []
		for i in range(0,10):
			lv.append((le[i] * la[i]) / 1000)
		
		vTotal = sum(lv) 
		
		self.v1.setText(str(lv[0]))
		self.v2.setText(str(lv[1]))
		self.v3.setText(str(lv[2]))
		self.v4.setText(str(lv[3]))
		self.v5.setText(str(lv[4]))
		self.v6.setText(str(lv[5]))
		self.v7.setText(str(lv[6]))
		self.v8.setText(str(lv[7]))
		self.v9.setText(str(lv[8]))
		self.v10.setText(str(lv[9]))
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
		tu = float(tu)/60
		
		#Tempo de Concentracao em h
		#PUXAR DE EMPIRICAS
		#N EH 1
		tc = 1
		
		#Tempo de Pico em h
		ta = tu/2 + 0.6 * tc
		
		#Convertendo para minutos e arredondando
		ta = ta * 60
		ta = int(ta)
		if(ta%10 < 5 and ta > 10):
			ta = ta - (ta%10)
		elif(ta%10 < 5 and ta > 10):
			ta = ta + (10 - ta%10)
		
		#Tempo de Base em h
		tb = 2.67 * ta
		
		#Convertendo para minutos e arredondando
		tb = tb * 60
		tb = int(tb)
		if(tb%10 < 5 and tb > 10):
			tb = tb - (tb%10)
		elif(tb%10 < 5 and tb > 10):
			tb = tb + (10 - tb%10)	
		
		#Vazao de Pico 
		areaTotal = 10
		vp = (0.75 * areaTotal * pUnitario)/(3.6 * ta)
		print(vp)
		
		#Arredondando
		vp = int(vp)
		if(vp%10 < 5 and vp > 10):
			vp = vp - (vp%10)
		elif(vp%10 < 5 and vp > 10):
			vp = vp + (10 - vp%10)
		
		print(ta)
		print(tb)
		print(vp)
		
		#Para a reta Ascendente
		a1 = 0
		b1 = float(vp)/float(ta)
		print(a1)
		print(b1)
		
		#Para a reta Descendente
		b2 = float((-vp))/float((tb-ta))		
		a2 = float(-tb * b2)
		print(a2)
		print(b2)

		#lista q ira conter a discretizacao
		ldiscretizacao = []
		#variavel para a discretizacao
		aux = 0
		
		#para a grafico eh em minutos
		tu = tu*60
		
		while(aux <= ta):
			ldiscretizacao.append(a1+(b1*aux))
			aux = aux + tu
		
		print(aux)	
		
		while(aux <= tb + tu):
			ldiscretizacao.append(a2+(b2*aux))
			aux = aux + tu
			
		print(aux)
		
		print('\n')
		print(ldiscretizacao)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
