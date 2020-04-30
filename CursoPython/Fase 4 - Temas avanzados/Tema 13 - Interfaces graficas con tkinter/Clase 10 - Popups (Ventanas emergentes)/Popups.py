from tkinter import *
from tkinter import messagebox as MessageBox

#Configuración de la raiz
root = Tk()

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

# Finalmente bucle de la aplicacion
root.mainloop()