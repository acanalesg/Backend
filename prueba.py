__author__ = 'carlos'

lista = ['nepal', 'katmandu']

def generar_literal(l):
    cadena = ""
    for elemento in lista:
        cadena += "elemento"
        cadena += " and "
        print elemento
    cadena = cadena[0:-4]


generar_literal(lista)