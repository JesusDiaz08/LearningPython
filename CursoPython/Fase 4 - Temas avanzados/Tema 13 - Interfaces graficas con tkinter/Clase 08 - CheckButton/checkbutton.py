# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:50:31 2020

@author: kaimo
"""

from tkinter import *

# 6 Nos ayudará a recuperar los valores de leche y azucar
def seleccionar():
	cadena = ""
	if leche.get():
		cadena += "Con leche"
	else:
		cadena += "Sin leche"
		
	if azucar.get():
		cadena += "y con azúcar"
	else:
		cadena += "y sin azúcar"
	
	monitor.config(text = cadena)

#Un usuario que diga, como quiere cafe
# 1. Configuración de la raíz
root = Tk()
root.title("Cafeteria")
root.config(bd = 15)

# 2. Almacenan las variables de los checkbutton
leche = IntVar()		# 1 si, 0 no
azucar = IntVar()		# 1 si, 0 no

# 4. Agregamos una imagen
imagen = PhotoImage(file = "imagen.gif")
Label(root, image = imagen).pack(side = "left")

# 5. Una vez hecho esto, vamos a crear un marco
# para poner allí los labels
frame = Frame(root)
frame.pack(side = 'right')

# Segundo Paso
Label(frame, text= '¿Cómo quieres el cafe?').pack(anchor = "w")
# 2,3 paso - onvalue : Valor cuando está clickado
# 2,3 paso - offvalue : Valor cuando no está clickado
# 6 - Añadimo command = seleccionar
Checkbutton(frame, text = 'Con leche', variable = leche, onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = "w")
Checkbutton(frame, text = 'Con azucar', variable = azucar, onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = "w")

# Ahora, vamos a recuperar los valores de leche y azucar
monitor = Label(frame)
monitor.pack()

# 1. Finalmente bucle de la aplicacion
root.mainloop()