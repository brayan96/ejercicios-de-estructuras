# -*- coding: utf-8 -*-
from pila import *

def operar(elemento, valor2, valor1):
    if elemento == "+":
        resultado = valor2 + valor1
    elif elemento == "-":
        resultado = valor2 - valor1
    elif elemento == "*":
        resultado = valor2 * valor1
    elif elemento == "/":
        resultado = valor2 / valor1

    return resultado
        
def evaluar(expresion2):
    pila = Pila()
    for elemento in expresion2:
        print(elemento)
        try:
            numero = float(elemento)
            pila.apilar(numero)

        except ValueError:
            print("op")
            if elemento not in "+-*/":
                raise ValueError("No esta el operador")
            try:
                valor1 = pila.desapilar()
                valor2 = pila.desapilar()
            except ValueError:
                raise ValueError("----")
           
            resultado = operar(elemento, valor2, valor1)
            pila.apilar(resultado)
      
    respuesta = pila.desapilar()

    if pila.es_vacia():
        return respuesta
    else:
        raise ValueError("----")

            
expresion1 = input("")

expresion2 = expresion1.split(" ")

print (evaluar(expresion2))

