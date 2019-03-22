# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:11:01 2019

@author: kaimorts
"""

import sys
if len(sys.argv) == 3:
    filas    = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if (filas and columnas) > 0 and (filas and columnas) < 10:
        for i in range(filas):
            print("\n")
            for j in range(columnas):
                print(" * ", end='')
    else:
        print("There was an error")
        print("Rows or columns are incorrect")
else:
    print("Error. Incorrects arguments.\nCorrect input is:")
    print("python name_program.py [1-9] [1-9]")