from ordenamientoSeleccion1 import OrdenamientoSeleccion
class PruebaOrdenamientoSeleccion:
	print("Ingrese el tamaño de numeros aleatorios que desea: ", end = '')
	tamanio = int(input())
	
	arregloOrden=OrdenamientoSeleccion(tamanio)
	print("Arreglo desordenado: ")
	print(arregloOrden.__repr__())
	arregloOrden.ordenar()
	print("arreglo ordenado: ")
	print(arregloOrden.__repr__())
	