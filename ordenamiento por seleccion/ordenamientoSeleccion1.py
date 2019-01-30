import random
class OrdenamientoSeleccion:
	datos = []

	def __init__(self, tamanio):
		for i in range(tamanio):
			self.datos.append(random.randrange(1000))

	def ordenar(self):
		for i in range(len(self.datos) - 1):
			masPequenio=i

			for indice in range(i+1, len(self.datos)):
				if self.datos[indice]<self.datos[masPequenio]:
					masPequenio=indice
			self.intercambiar(i,masPequenio)
			self.imprimirPasada(i+1,masPequenio)

	def intercambiar(self, primero, segundo):
		temporal = self.datos[primero]
		self.datos[primero] = self.datos[segundo]
		self.datos[segundo] = temporal

	def imprimirPasada(self, pasada, indice):
		print("despues de pasada ", pasada, ": ", end='')
		
		for i in range(indice):
			print(self.datos[i], " ", end='')
		print(self.datos[indice], "* ", end='')

		for i in range(indice + 1, len(self.datos)):
			print(self.datos[i], " ", end='')
		print("\n             ", end='')	
		
		for j in range(pasada):
			print("--  ", end='')
		print()

	def __repr__(self):
		temporal=""
		for elemento in range(len(self.datos)):
			temporal += str(self.datos[elemento]) + " "
		
		return temporal + "\n"

