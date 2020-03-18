# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:44:26 2020

@author: kaimorts
"""
from io import open
import pickle

def leer():
  nombre_fichero = 'personas.txt'
  modo = 'r' 
  fichero = open(nombre_fichero, modo)  #,  encoding="utf8"
  lineas = fichero.readlines()
  fichero.close()
  
  return lineas

def transformar(lineas):
  personas = []
  for linea in lineas:
    campos = linea.replace("\n", "").split(';')
    persona = {"id"         : campos[0], 
               "nombre"     : campos[1],
               "apellido"   : campos[2],
               "nacimiento" : campos[3]
               }
    personas.append(persona)
  
  return personas

def mostrar(personas):
  for persona in personas:
    for clave,valor in persona.items():
      print("{}:{:>12}".format(clave, valor))
    print("================\n")
    

lineas = leer()
personas = transformar(lineas)
mostrar(personas)


  