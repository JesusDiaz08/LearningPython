# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:50:33 2019

@author: kaimorts
@curso : Curso Python de Udemy
"""

""" SI A ESTE SCRIPT NO SE LE PASAN LOS ARGUMENTOS QUE REQUIERE, EL PROGRAMA VA A FALLAR
    python segundo_script.py  'argumento'       5
    Para evitar errores con respecto a los argumentos que se tienen que enviar
    podemos verificar la longitud de la lista y ver si cumple
"""

import sys

if len(sys.argv) == 3:
    nombre_script = sys.argv[0]
    texto         = sys.argv[1]
    repeticiones  = int(sys.argv[2])

    print("Numero de repeticiones: ", repeticiones)
    
    for r in range(repeticiones):
       # print(r+1, "\tNombre script: ", nombre_script)
        print("\t", texto)
else:
    print("Error. Introduce los argumentos correctamente.")
    print("python segundo_script.py  'argumento'       5")