# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:55:31 2020

@author: kaimo
"""

from tkinter import *

# Radiobutton: Cuando quieres proporcionarle una opción entre varias
# - Tiene un valor por defecto: 1,2,3,....,N

def reset():
  opt.set(None)
  monitor.config(text = "")

def selection():
  monitor.config(text = "{}".format(opt.get()))
  
#Configuracion de la raiz
root = Tk()

opt = IntVar()

rb1 = Radiobutton(root, text = 'Opt 1', variable=opt, value = 1, command = selection)
rb1.pack()
rb2 = Radiobutton(root, text = 'Opt 2',variable=opt, value = 2, command = selection)
rb2.pack()
rb3 = Radiobutton(root, text = 'Opt 3', variable=opt, value = 3, command = selection)
rb3.pack()

monitor = Label(root)
monitor.pack()

restart = Button(root, text = 'Reiniciar', command = reset)
restart.pack()


# Finalmente bucle de la aplicacion
root.mainloop()
