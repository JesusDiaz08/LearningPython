# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:43:15 2020

@author: kaimo
"""
from io import open
import sys

def leer():
  nombre_fichero = "contador.txt"
  modo = 'a+'  # Si no existe, lo crea y da acceso de lectura con el +
  fichero = open(nombre_fichero, modo)
  fichero.seek(0)  # Inicializamos el puntero al inicio
  contador = fichero.readline()
  if len(contador) == 0:  # Esta vacio
    contador = "0"
    fichero.write(contador)
    
  fichero.close()  
  return contador
  
def guardar(contador):
  nombre_fichero = "contador.txt"
  modo = 'w'
  fichero = open(nombre_fichero, modo)
  fichero.write(str(contador))
  fichero.close()

def modificar():
  try:
    contador = int(leer())
    if len(sys.argv) == 2:
      if sys.argv[1] == 'inc':
        contador += 1
      elif sys.argv[1] == 'dec':
        contador -= 1    
    print(contador)
    guardar(contador)
  except:
    print("Error. Fichero corrupto")    
  
modificar()