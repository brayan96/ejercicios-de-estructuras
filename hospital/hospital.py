# -*- coding: utf-8 -*-

import cola
import paciente

class Hospital():
    def __init__(self):
        self.fila = cola.Cola()

    def crearPaciente(self, nombre, ident, especialidad):
        cliente = paciente.Paciente(nombre, ident, especialidad)
        self.fila.encolar(cliente)

    def atenderPaciente(self):
        pac_aten = self.fila.desencolar()
        print ("paciente " + pac_aten.getNombre())
        print ("identificado con " + pac_aten.getId())
        print ("ubicado en " + pac_aten.getEspecialidad())
        print ("fue atendido")
        print ("--------- o ----------")
