# -*- coding: utf-8 -*-

class Paciente():
    def __init__(self, nombre, ide, especialidad):
        self.nombre = nombre
        self.ide = ide
        self.especialidad = especialidad
		
    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.ide

    def getEspecialidad(self):
        return self.especialidad
