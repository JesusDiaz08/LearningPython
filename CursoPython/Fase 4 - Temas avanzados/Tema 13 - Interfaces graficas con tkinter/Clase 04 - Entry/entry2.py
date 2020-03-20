from tkinter import *

root = Tk()

# Disposicion automatica de cuadricula
# Arriba a la izquierda - LBL_NOMBRE
label = Label(root, text = 'Nombre muy largo:')
label.grid(row = 0, column = 0)
label.grid(sticky = "e", padx=5, pady=5)  # Nos permite justificar la etiqueta,identar, a la derecha

# padx = nos permite ajustar 5 pixeles horizontal
# pady = nos permite ajustar 5 pixeles vertical

# Arriba a la derecha - ENTRY_NOMBRE
# justify - Justificar a la derecha el texto del entry
# state - Nos permite habilitar o deshabilitar un estado
entry = Entry(root)
entry.grid(row = 0, column = 1, padx=5, pady=5)
entry.config(justify = 'right', state = 'disabled') 


# Abajo a la izquierda - LBL_APELLIDO
label2 = Label(root, text = 'Apellido:')
label2.grid(row = 1, column = 0)
label2.grid(sticky = "e", padx=5, pady=5)  # Nos permite justificar la etiqueta,identar, a la derecha

# Abajo a la derecha - ENTRY_APELLIDO
entry2 = Entry(root)
entry2.grid(row = 1, column = 1, padx=5, pady=5)
entry2.config(justify = 'left')  # Justificar a la derecha

# Que pasa si queremos escribir una contraseña
# Debemos usar el parametro >>show<< y el caracter 
label3 = Label(root, text = 'Password')
label3.grid(row = 2, column = 0)
label3.grid(sticky = "e", padx = 5, pady = 5)

entry3 = Entry(root)
entry3.grid(row = 2, column = 1, padx = 5, pady = 5)
entry3.config(justify = 'center', show = "?")

root.mainloop()
