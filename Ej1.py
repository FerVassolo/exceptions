"""Defina en Python una función para calcular el factorial de un número natural.
Dada la siguiente lista: lista = [ 10 , -5 , 1.2 , 'apple' ],
calcule el factorial para cada elemento.
Maneje las excepciones TypeError y ValueError.
"""

lista = [10, -5, 1.2, 'apple']

def factorial(a):

        if a == 0 or a ==1:
            return a
        elif a > 1:
            return a*factorial(a-1)


for elm in lista:
    try:
        factorial(elm)
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    else:
        print("Introducí nro entero")

