
from tkinter import Tk

class Window:
	__title = "Analysis Image"

	def __init__(self):
		root = Tk()
		title = self.getTitle()
		root.title(title)			# Set the window's title
		root.resizable(0,0)   # Can not resizeable the window
		root.iconbitmap('../hola.ico')  # Set image like icono
		root.mainloop()   # Display the window

	def getTitle(self):
		return self.__title

	def setTitle(self, title):
		self.__title = title

w = Window()

