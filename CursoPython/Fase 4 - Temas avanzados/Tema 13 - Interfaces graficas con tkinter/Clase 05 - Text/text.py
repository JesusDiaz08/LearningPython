from tkinter import *

# Configuracion de la raiz
root = Tk()

# Agregamos un campo de texto
texto = Text(root)
texto.pack()

# width = N - Indica que podemos escribir hasta N caracteres horizontalmente
# height = M - Indica que podemos escribir hasta M caracteres verticalmente
texto.config(width = 30, height = 10)

# Cambiamos la fuente
# Cambiamos el padding - el borde entre contenido y el widget
texto.config(font = ("Consolas", 12), padx = 15, pady = 15)

# Establecer un color para texto seleccionado
texto.config(selectbackground = 'red')

root.mainloop()
