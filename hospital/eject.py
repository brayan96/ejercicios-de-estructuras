# -*- coding: utf-8 -*-

import hospital

def eject():
    clinica = hospital.Hospital()
    clinica.crearPaciente("Andres", "1024", "pediatria")
    clinica.crearPaciente("Camila", "2135", "geriatria")
    clinica.crearPaciente("Carlos", "6235", "neumologia")
    clinica.crearPaciente("Daniel", "0831", "psiquiatria")
    clinica.crearPaciente("Valentina", "1025", "oftalmologia")
    clinica.crearPaciente("Sandra", "1025", "traumatologia")
    clinica.atenderPaciente()
    clinica.atenderPaciente()
    clinica.atenderPaciente()
    clinica.atenderPaciente()

eject()
