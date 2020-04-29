# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:50:31 2020

@author: kaimo
"""

from tkinter import *

#Un usuario que diga, como quiere cafe

# Configuración de la raíz
root = Tk()
root.title("Cafeteria")
root.config(bd = 15)

leche = IntVar()   # 1 - sí, 0 - no
azucar = IntVar()  # 1 - sí, 0 - no





lbl_cafe = Label(root, text = '¿Cómo quieres el café?')
lbl_cafe.pack()

cb_leche = Checkbutton(root, text = 'Con leche', variable = leche, onvalue = 1, offvalue = 0)
cb_leche.pack()

cb_azucar = Checkbutton(root, text = 'Con azucar', variable = azucar, onvalue = 1, offvalue = 0)
cb_azucar.pack()


# Finalmente bucle de la aplicacion
root.mainloop()