from tkinter import *

# Configuracion de la raíz
root = Tk()

# Vamos a crear un menu superior

# 1. Creamos menu
# Nota: El menu no se empaqueta, ya que está siempre en la
#       misma posición, aunque haya submenus. Al menu global
#		se le suele conocer como 'menubar'
menubar = Menu(root)
root.config(menu = menubar)

# 2. Vamos a crear unos cuantos submenus
# 4. Quitamos el submenu por defecto, el de [--]
#	 Eso lo hacemos de la siguiente manera
#	 tearoff = 0
# 5. Añadir elementos a los submenús
#    Estos elementos son los >> comandos <<
file_menu = Menu(menubar, tearoff = 0)
# 5. Añadir elementos usando la función >> add_command <<
file_menu.add_command(label = "New File")
file_menu.add_command(label = "Open")
file_menu.add_command(label = "Save")
file_menu.add_command(label = "Close")
# 6. Vamos a crear un separador entre elementos
#    Esto se va a lograr usando la función 
# 	 >> add_separator() <<
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

edit_menu = Menu(menubar, tearoff = 0)
# 5. Añadir elementos a los submenús
#    Estos elementos son los >> comandos <<
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Paste")

help_menu = Menu(menubar, tearoff = 0)
# 5. Añadir elementos a los submenús
#    Estos elementos son los >> comandos <<
help_menu.add_command(label = "Welcome")
help_menu.add_command(label = "Help")
help_menu.add_command(label = "Documentation")
help_menu.add_separator()
help_menu.add_command(label = "About")

# 3. Añadimos el texto de cada submenu
menubar.add_cascade(label = "File", menu = file_menu)  # Añadimos un menu en cascada
menubar.add_cascade(label = "Edit", menu = edit_menu)  # Añadimos un menu en cascada
menubar.add_cascade(label = "Help", menu = help_menu)  # Añadimos un menu en cascada

#Finalmente bucle de la aplicación
root.mainloop()