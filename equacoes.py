import sys 
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

from ui_equacoes import Ui_Dialog 
from bransby import Ui_Bransby 
from kirpich1 import Ui_Kirpich1 
from kirpich2 import Ui_Kirpich2 
from kerby import Ui_Kerby 
from scs import Ui_Scs

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
		
class equacoes(QtGui.QDialog, Ui_Dialog):
	def __init__(self, parent=None):
		super(equacoes, self).__init__(parent)
		self.setupUi(self)
        
		self.CalculaIDF.clicked.connect(self.idfCalculo)	
		
		self.scs.clicked.connect(self.scsCalculo)
		
		self.kirpich1.toggled.connect(self.calKirpich1)
		self.kirpich2.toggled.connect(self.calKirpich2)
		self.kerby.toggled.connect(self.calKerby)
		self.bransby.toggled.connect(self.calBransby)

	def calKirpich1(self, enabled):
		if enabled:
			w = Kirpich1()
			w.show()
			#rever	
			app.exec_()

	def calKirpich2(self, enabled):
		if enabled:
			w = Kirpich2()
			w.show()
			#rever	
			app.exec_()
					
	def calKerby(self, enabled):
		if enabled:
			w = Kerby()
			w.show()
			#rever	
			app.exec_()
	
	def calBransby(self, enabled):
		if enabled:
			w = Bransby()
			w.show()
			#rever	
			app.exec_()
				
	def idfCalculo(self):
		#lendo variaveis
		k = self.k.value()
		t0 =  self.t0.value()
		m = self.m.value()
		n = self.n.value()
		Tr = self.Tr.value()
		t = self.t.value()
		
		#nome do lugar 
		city = self.City.text()
		estado = self.Estado.text()	

		#IDF'S CALCULO
		intervalo = 0
		cont = 0
		#criando lista vazia
		lintensidade = []
		lintervalo = []
		#calcula a intensidade com os intervalos de 30 em 30 minutos 
		while intervalo < t:
			intervalo = intervalo + 30
			lintervalo.append(intervalo)
			i = (k * (Tr**m)) / ((intervalo + t0)**n)
			lintensidade.append(i)

		#zerando o contador
		intervalo = 0 
		#criando lista vazia
		lprecipitacao = []
		#para precorrer a list
		#e contar quantos parametros tem 
		#calcula a precipitacao com a intesidade
		while intervalo < t:
			intervalo = intervalo + 30
			lprecipitacao.append((lintensidade[cont]*intervalo))
			cont = cont + 1

		#o primeiro premanece o msm
		auxCont = 1
		lprecipitacaoDiferenca = []
		lprecipitacaoDiferenca.append(lprecipitacao[0])

		#diferenca da precipitacao
		while auxCont < cont:
			lprecipitacaoDiferenca.append(lprecipitacao[auxCont] - lprecipitacao[auxCont-1])
			auxCont = auxCont + 1
		
		#blocos alternados 
		#nao pode ser vazia
		#numeros so para garantir o tamanho da lista, para a insercao ser correta
		lblocosAlternados = range(auxCont)
		lprecipitacaoDiferenca.sort()
		
		lblocosAlternados = lprecipitacaoDiferenca[::2]
		lblocosAlternados += list(reversed(lprecipitacaoDiferenca[1::2]))
			
		#GRAFICO
		w = QtGui.QWidget()
		
		plot = pg.PlotWidget()
		plot.plot(lintervalo, lblocosAlternados)

		layout = QtGui.QGridLayout()
		w.setLayout(layout)

		layout.addWidget(plot, 0, 1, 3, 1)

		#display graphic 
		w.show()
		#rever
		app.exec_()

	def scsCalculo(self):
		#lendo variaveis
		k = self.k.value()
		t0 =  self.t0.value()
		m = self.m.value()
		n = self.n.value()
		Tr = self.Tr.value()
		t = self.t.value()
		
		#IDF'S CALCULO
		intervalo = 0
		cont = 0
		#criando lista vazia
		lintensidade = []
		lintervalo = []
		#calcula a intensidade com os intervalos de 30 em 30 minutos 
		while intervalo < t:
			intervalo = intervalo + 60
			lintervalo.append(intervalo)
			i = (k * (Tr**m)) / ((intervalo + t0)**n)
			lintensidade.append(i)

		print(lintensidade)

		#zerando o contador
		intervalo = 0 
		#criando lista vazia
		lprecipitacao = []
		#para precorrer a list
		#e contar quantos parametros tem 
		#calcula a precipitacao com a intesidade
		while intervalo < t:
			intervalo = intervalo + 60
			#rever
			lprecipitacao.append((lintensidade[cont]*intervalo))
			cont = cont + 1

		#o primeiro premanece o msm
		auxCont = 1
		lprecipitacaoDiferenca = []
		lprecipitacaoDiferenca.append(lprecipitacao[0])

		#diferenca da precipitacao
		while auxCont < cont:
			lprecipitacaoDiferenca.append(lprecipitacao[auxCont] - lprecipitacao[auxCont-1])
			auxCont = auxCont + 1
		
		#blocos alternados 
		#nao pode ser vazia
		#numeros so para garantir o tamanho da lista, para a insercao ser correta
		lblocosAlternados = range(auxCont)
		lprecipitacaoDiferenca.sort()
		
		lblocosAlternados = lprecipitacaoDiferenca[::2]
		lblocosAlternados += list(reversed(lprecipitacaoDiferenca[1::2]))
		
		#mostrar pagina
		#corrigir
		w = Scs(lintensidade, lblocosAlternados)
		w.show()
		#rever	
		app.exec_()
	
def main():	
	app = QtGui.QApplication(sys.argv)	
	ex = equacoes()	
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
