# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:32:23 2020

@author: kaimo
"""

from tkinter import *

def limpiarScreen():
  A.set("")
  B.set("")

def sumar():
  R.set( float(A.get()) + float(B.get()) )
  limpiarScreen()

def restar():
  R.set( float(A.get()) - float(B.get()) )
  limpiarScreen()

def multiplicar():
  R.set( float(A.get()) * float(B.get()) )
  limpiarScreen()

# Configuracion de la raiz
root = Tk()
root.config(bd = 15)

A = StringVar()
B = StringVar()
R = StringVar()

labelA = Label(root, text = "Numero1")
labelA.pack()

valueA = Entry(root, justify = "center", textvariable = A)
valueA.pack()

labelB = Label(root, text = "Numero2")
labelB.pack()

valueB = Entry(root, justify = "center", textvariable = B)
valueB.pack()

labelres = Label(root, text = "\nResultado")
labelres.pack()

# El parametro disable es para que el resultado no se modifique
result = Entry(root, justify = "center", textvariable = R, state = "disabled")
result.pack()

#=============== APARECERAN EN BLOQUE, UNO DEBAJO DE OTOR =========================
'''
botonSuma = Button(root, text = "Sumar", command = sumar)
botonSuma.pack()  # Asi no sucede nada

botonResta = Button(root, text = "Restar", command = restar)
botonResta.pack()  # Asi no sucede nada

botonMult = Button(root, text = "Multiplicar", command = multiplicar)
botonMult.pack()  # Asi no sucede nada
'''
#==================================================================================

#=============== APARECERAN EN LA MISMA FILA =========================
botonSuma = Button(root, text = "Sumar", command = sumar)
botonSuma.pack(side = "left")  # Asi no sucede nada

botonResta = Button(root, text = "Restar", command = restar)
botonResta.pack(side = "left")  # Asi no sucede nada

botonMult = Button(root, text = "Multiplicar", command = multiplicar)
botonMult.pack(side = "left")  # Asi no sucede nada
#==================================================================================




# Finalmente bucle de la aplicación
root.mainloop()