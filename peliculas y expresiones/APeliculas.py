# -*- coding: utf-8 -*-

from pila import *

class Peliculas:

    def __init__(self,year,genero,titulo):
        self.year=year
        self.genero=genero
        self.titulo=titulo

def menuGenero():
    print("Comedia")
    print("Fantasia")
    print("Accion")
    print("Terror")
    
valida = True

while valida:
    pila = Pila()
    
    pila.apilar(Peliculas(2001,"Fantasia","HP"))
    pila.apilar(Peliculas(2001,"Fantasia","Cronicas de Narnia"))
    pila.apilar(Peliculas(2012,"Terror","El Aro"))
    pila.apilar(Peliculas(2013,"Terror","Saw 7"))
    pila.apilar(Peliculas(2010,"Terror","El Conjuro"))
    pila.apilar(Peliculas(2016,"Accion","Duro de Matar"))
    pila.apilar(Peliculas(2000,"Accion","Día de la Independencia"))
    pila.apilar(Peliculas(2004,"Comedia","Tontos y Retontos"))
    pila.apilar(Peliculas(2007,"Comedia","American Pie"))

    menuGenero()
    consulta = input("\nIngrese Genero o Titulo de pelicula a Consultar: ")
    
    while pila.es_vacia() == False:
        pelicula = pila.desapilar()
        
        if pelicula.genero == consulta:
            print("Titulo de la pelicula: " + pelicula.titulo)

        elif pelicula.titulo == consulta:
            print ("La pelicula pertenece al genero de: "+ pelicula.genero)
            
    valida = ("s" == input("\nConsultar de Nuevo S/N").lower())
