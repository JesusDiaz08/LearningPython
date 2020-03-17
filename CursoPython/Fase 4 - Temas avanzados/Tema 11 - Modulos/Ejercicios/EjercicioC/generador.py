# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:05:50 2020

@author: kaimo
"""
import random
import math

def leer_numero(ini, fin, mensaje):
  while(True):
    try:
      valor = int(input(str(mensaje)))
    except:
      print("Error. Número no válido.")
    else:
      if valor >= ini and valor <= fin:
        break     
  
  return valor


def generador():
  numeros = leer_numero(1,20, "¿Cuantos números quieres generar? [1-20]: ")
  modo = leer_numero(1,3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
  
  lista = []
  for i in range(numeros):
    numero = random.uniform(0, 100 + 1)
    if modo == 1:
      num_round = math.ceil(numero)
      print("{} => {}".format(numero, num_round))
      
    elif modo == 2:
      num_round = math.floor(numero)
      print("{} => {}".format(numero, num_round))
      
    elif modo == 3:
      num_round = round(numero)
      print("{} => {}".format(numero, num_round))
    
    lista.append(num_round)
  
  return lista  

generador()
  
  