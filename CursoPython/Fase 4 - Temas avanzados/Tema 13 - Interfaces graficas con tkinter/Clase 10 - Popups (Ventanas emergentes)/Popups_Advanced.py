from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#Configuración de la raiz
root = Tk()

"""
def showinfo():
	title = "Hola"
	msg = "Hola Mundo"
	MessageBox.showinfo( title , msg )

def showwarning():
	title = "Alerta"
	msg = "Sección solo para administradores"
	MessageBox.showwarning( title , msg )

def showerror():
	title = "Error"
	msg = "Ha ocurrido un error inesperado"
	MessageBox.showerror( title , msg )

def ask_question():
	title = "Salir"
	msg = "¿Está seguro que quiere salir sin guardar?"
	# La función askquestion nos devuelve un valor para saber la opcion escogida
	# - Regresa un string con la palabra "Yes" o "No"
	opt = MessageBox.askquestion( title , msg )
	if opt == "yes":  # "no"
		root.destroy()
	
def ask_ok_cancel():
	title = "Guardar"
	msg = "¿Deseas guardar los cambios actuales?"
	# La función askokcancel nos devuelve un valor para saber la opcion escogida
	# - Regresa un boolean con True o False
	opt = MessageBox.askokcancel( title , msg )
	if opt:  # "no"
		root.destroy()

def ask_yesno():
	title = "Salir"
	msg = "¿Está seguro que quiere salir sin guardar?"
	# La función >>askyesno<< nos devuelve un valor para saber la opcion escogida
	# Es muy parecido a la funcion >> askquestion << pero en vez de retornar
	#   un string, nos devuelve un boolean: True o False
	opt = MessageBox.askyesno( title , msg )
	if opt:
		root.destroy()

def ask_retry_cancel():
	title = "Conectar"
	msg = "No se ha establecido la conexión"
	# La función >>askretrycancel<< nos devuelve un valor para saber la opcion escogida
	# esta función devuelve un booleano: True o False
	opt = MessageBox.askretrycancel(title, msg)
	if opt == False: # Si escogemos cancelar
		root.destroy()

# 2. Popup para mostrar información
Button(root, text = "Info", command = showinfo).pack()

# 3. Popup para mostrar un warning
Button(root, text = "Warning", command = showwarning).pack()

# 4. Popup para mostrar un error
Button(root, text = "Error", command = showerror).pack()

# 5. Popoup para ask_question : Nos devuelve un valor - Si o No
Button(root, text = "Salir", command = ask_question).pack()

# 6. Popup para ask_ok_cancel: Realiza una pregunta para "Aceptar" o "Cancelar"
Button(root, text = "Guardar", command = ask_ok_cancel).pack()

# 7. Popoup para ask_yes_no : Nos devuelve un valor - True o False
Button(root, text = "Salir v2", command = ask_yesno).pack()

# 8. Popo para ask_retry_cancel: Nos ayuda a preguntar al usuario si desea >> reintentar algo <<
Button(root, text = "Conectarse", command = ask_retry_cancel).pack()
"""

def color_chooser():
	title = "Elige un color"
	# La funcion >> askcolor << devuelve el color seleccionado
	# Devuelve una tupla con dos elementos:
	# Al seleccionar Aceptar:
	#   1er elemento : Una tupla haciendo referencia en RGB
	#   2o elemento  : Valor hexadecimal del color
	# Al seleccionar Cancel:
	#	Retorna una tupla con Nones: (None, None)
	color = ColorChooser.askcolor(title = title)
	print(f"Color {color}")

def file_dialog():
	title 		= "Abrir un fichero"
	initial_dir = "C:/"
	#Filtro de extensiones para permitir solo ciertas extensiones
	# Si solo se agrega un filtro, al final de la tupla se deja una ','
	file_types  = (("Ficheros de texto", "*.txt"),
				   ("Ficheros de pdf", "*.pdf"),
				   ("Todos los ficheros", "*.*")) 
	# La función >>askopenfilename> nos permite 
	# conseguir la ruta de un fichero para poder abrirlo o guardarlo
	# Nos devuelve una cadena de caracteres - La ruta al fichero
	# Esta es la que se necesita para abrirlo usando open
	# Y si no seleccionamos nada, nos da una cadena vacia
	ruta = FileDialog.askopenfilename(title = title, initialdir = initial_dir, filetypes = file_types)
	print(f"Ruta: {ruta}")

def saves_as_file():
	title = "Guardar un fichero"
	# Nos ayuda a guardar un fichero que nosotros queramos
	# Si le damos cancelar, nos regresa "None", 
	# Si le damos aceptar, nos regresa "un fichero abierto"
	#   que contiene las siguientes propiedades:
	#	1. name : Nos da la ruta donde se guarda
	#	2. mode : w: Modo de escritura
	#   3. encoding
	# Podemos indicar algunos paramentros, como en la 
	#   función >> file_dialog << o indicarle otros, como:
	#    - mode = "a"  - Append
	#	 		  "r+" - Lectura y escritura, con cursor al principio
	# 	 - defaultextension = ".txt"
	_mode  = "w" # Lecutra y escritura, con cursor al inicio
	_dfext = ".txt"  # Extension por default para guardarlo al momento de crearlo
	fichero = FileDialog.asksaveasfile(title = title, mode = _mode, defaultextension = _dfext)  # Equivale a open('ruta', 'w')
	print(f"Fichero: {fichero}")
	if fichero is not None:
		fichero.write("Prueba en función >>save_as_file<< !")  # Se puede hacer por el mode = "r+"
		fichero.close()

# 9. Popup para color_chooser : Nos permite escoger un color de una paleta de colores
Button(root, text = "Select color", command = color_chooser).pack()

# 10. Pop para file_dialog : Nos permite obtener la ruta de un archivo o fichero
Button(root, text = "File dialog", command = file_dialog).pack()

# 11. Pop para : Buscar un directorio para guardar un archivo o fichero
Button(root, text = "Guardar como", command = saves_as_file).pack()

# Finalmente bucle de la aplicacion
root.mainloop()