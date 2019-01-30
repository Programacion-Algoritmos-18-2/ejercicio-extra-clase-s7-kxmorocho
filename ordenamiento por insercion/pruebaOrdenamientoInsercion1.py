from ordenamientoInsercion1 import OrdenamientoInsercion
class PruebaOrenamientoInsercion:
	
	valores = [23, 45, 56, 9]

	arregloOrden=OrdenamientoInsercion(valores)
	print("Arreglo desordenado: ")
	print(arregloOrden.__repr__())

	arregloOrden.sort()
	print("Arreglo ordenado: ")
	print(arregloOrden.__repr__())
	

