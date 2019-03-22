# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:57:08 2019

@author: kaimorts
"""
import sys
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero >= 0 and numero <= 9999:
        cadena = str(numero)
        longit = len(cadena)
        
        for i in range(longit):
            print("{:04d}".format(int(cadena[longit - i - 1]) * (10 ** i)))
        
        
    else:
        print("El rango de numeros es de 0 a 9999")
    
else:
    print("Entrada incorrecta.")
    print("La manera correcta de meter los datos es: ")
    print("python descomposicion.py [0-9999]")
