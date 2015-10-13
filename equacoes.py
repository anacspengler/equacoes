import sys 
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

#import ui part from equacoes
from ui_equacoes import Ui_Dialog 

#import class from empiricas
from empiricas import Kirpich1
from empiricas import Kirpich2
from empiricas import Kerby
from empiricas import Bransby

from scs_ import Scs
				
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

		#print(lintensidade)

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
		
		self.precipitacao = sum(lblocosAlternados)
		
		#mostrar pagina
		#corrigir
		w = Scs(self.precipitacao)
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
