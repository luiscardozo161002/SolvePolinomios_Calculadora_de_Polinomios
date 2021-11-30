#Importamos la libreria SympY para usar variables simbolicas (x, y)
import sympy

#Obtenes los dos polinomios introducidos por el usuario
P1 = input("Ingrese el primer Polinomio: ")
P2 = input("Ingrese el segundo Polinomio: ")
print("\n")

#Definimos los simbolos
sympy.init_printing()
x,y = sympy.symbols('x,y')

#Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy.
Poly1 = sympy.Poly(P1)
Poly2 = sympy.Poly(P2)

#Declaramos una funcion para cada operacion que querramos utilizar

def mult(p1, p2):
	return p1 * p2

def suma(p1, p2):
	return p1 + p2

def res(p1, p2):
	return p1 - p2

def div(p1, p2):
	return p1 / p2

#Guardamos los valores retornados por las funciones y les pasamos los 2 polinomios como parametros,  Poly1 y Poly2
resultadoMult = mult(Poly1, Poly2)
resultadoSuma = suma(Poly1, Poly2)
resultadoDiv = div(Poly1, Poly2)
resultadoRes = res(Poly1, Poly2)


#Mostramos el valor que deseemos
print("Resultado: ",resultadoSuma)
