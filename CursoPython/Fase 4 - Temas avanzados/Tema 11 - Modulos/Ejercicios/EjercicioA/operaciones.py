# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:35:32 2020

@author: kaimorts
"""
def suma(a,b):
  try:
    res = a + b
  except TypeError:
    print("Error. Tipo de dato no válido")
  else: 
    return res

def resta(a,b):
  try:
    res = a - b
  except TypeError:
    print("Error. Tipo de dato no válido")
  else: 
    return res

def producto(a,b):
  try:
    res = a * b
  except TypeError:
    print("Error. Tipo de dato no válido")
  else: 
    return res

def division(a,b):
  try:
    res = a / b
  except TypeError:
    print("Error. Tipo de dato no válido")
  except ZeroDivisionError:
    print("Error. No es posible dividir entre cero")
  else: 
    return res