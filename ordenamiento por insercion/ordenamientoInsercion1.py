import random
class OrdenamientoInsercion:
	
	datos=[]
	
	def __init__(self, valores):
		
		datos = valores

	def sort(self):
		for siguiente in range(1, len(self.datos)):
			insercion = self.datos[siguiente]
			moverElemento = siguiente
			while moverElemento > 0 and self.datos[moverElemento - 1] > insercion:
				self.datos[moverElemento] = self.datos[moverElemento - 1]
				moverElemento -= 1
			self.datos[moverElemento] = insercion	
			self.imprimirPasada(siguiente, moverElemento)

	def imprimirPasada(self, pasada, indice):
		print("despues de pasada ", pasada, end='')
		
		for i in range(indice):
			print(self.datos[i], " ", end='')
		print(self.datos[indice], "* ", end='')
		
		for i in range(indice + 1, len(self.datos)):
			print(self.datos[i], " ", end='')
		print("\n             ", end='')	

		for i in range(pasada+1):
			print("--  ", end='')
		print()

	def __repr__(self):
		temporal=""
		for elemento in range(len(self.datos)):
			temporal += str(self.datos[elemento]) + " "
		
		return temporal + "\n"
