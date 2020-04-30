from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

"""
@author: Jesus Diaz
@date: April 29th, 2020
@description: Building a text editor using tkinter 
			  with different widgets
"""

path = ""   # It will use to storage the file's path
_dir = {"current" : "."}
_filetype = {"files_text" : ("Files text", "*.txt")}
_mode = {"read"   : "r",
		"write"	  : "w",
		"write+"  : "w+",
		"append" : "a"
		}

# |=============== >> FUNCTION FOR MENU BAR << SECTION ===============|
# 8.
def new_file():
	global path   # 8.1 Specifying that "path" is a "global" variable
	msg_lwm.set("> New File")
	path = ""	  # 8.3 Changing the global path variable
	# 8.4 Deleting the text-box content
	text.delete(1.0, "end")  # 1.0 indicate from the start and with "end" indicate the end jaja 
	# Changing the window's title
	root.title("Kai-text")

def open_file():
	global path
	global _dir
	global _filetype
	global _mode
	msg_lwm.set("> Open File")
	path = FileDialog.askopenfilename(
		initialdir = _dir["current"], 
		filetype   = ( _filetype["files_text"],),
		title = "Open a file text")
	
	if path != "":
		file = open(path, _mode["read"])
		content = file.read()
		text.delete(1.0, "end")    # Deleting the text-box content
		text.insert("insert", content)  # Inserting the file-opened's content to the text-box
		file.close()
		# Changing the window's title
		root.title(path + "- Kai-text")

def save_file():
	global path
	global _mode
	msg_lwm.set("> Save File")
	
	# Case 01 : The file has been opened from "Open" tab, then it already existed
	# We already have one "path", then we have to verify it.
	if path != "":
		# "end-1c" specifies that it retrieves all the text, 
		# but does not add a new line. Because there is an error 
		# every time I open and save, since it is adding blank lines
		# "-1c" tell us that it is the last character - linea-break
		content = text.get(1.0, "end-1c")	# Recovery all the content
		file = open(path, _mode["write+"])
		file.write(content)
		file.close()
		msg_lwm.set("> File saved successfully")
	
	# Case 02 : The file is a new file, then it did not already existed previously
	else:
		saveas_file()

def saveas_file():
	global path
	global _mode
	msg_lwm.set("> Save As...")
	file = FileDialog.asksaveasfile(title = "Save file", mode = _mode["write"], defaultextension = ".txt")
	if file is not None:
		path = file.name    # Getting the file's path
		# "end-1c" specifies that it retrieves all the text, 
		# but does not add a new line. Because there is an error 
		# every time I open and save, since it is adding blank lines
		# "-1c" tell us that it is the last character - linea-break
		content = text.get(1.0, "end-1c")	# Recovery all the content
		file = open(path, _mode["write+"])
		file.write(content)
		file.close()
		msg_lwm.set("> File saved successfully")
	else:
		msg_lwm.set("Saving as canceled")
		path = ""

# |===================================================================|

# Root configuration
root = Tk()

# |=============== MENU BAR SECTION ===============|
# @description: Creating a menu bar with only one tab
#				"File" which contains 5 events (commands):
#				New, Open, Save, Save As... and Exit

# 1. Adding a title on the root
root.title("Kai-text")
# 2. Creating a superior menu
menu_bar = Menu(root)
# 3. Adding the >> File << tab
file_menu = Menu(menu_bar, tearoff = 0)
#   3.1 Create a new file text
file_menu.add_command(label = "New", command = new_file)
#	3.2 Open a file text
file_menu.add_command(label = "Open", command = open_file)
#   3.3 Save the current file text
file_menu.add_command(label = "Save", command = save_file)
#	3.4 Saves as one file text
file_menu.add_command(label = "Save As...", command = saveas_file)
#   3.5 Adding a separator
file_menu.add_separator()
#	3.6 Exit from program
file_menu.add_command(label = "Exit", command = root.quit)
# 4. >> menu_bar << adds >> file_menu <<
menu_bar.add_cascade(menu = file_menu, label = "File")

# |================================================|


# |=============== TEXT BOX SECTION ===============|
# @decription: Text-box allow us to type any content
#			   we need to create a text file

# 6. Creating a central text box
text = Text(root)
text.pack(fill="both", expand = 1)  # It should be occupied the same size as root
#	6.1 Specifying type and size of font
type_font = "Consolas"
size_font = 12
text.config(bd = 0, padx = 6, pady = 4, font = (type_font, size_font))

# |================================================|


# |================ MONITOR SECTION ===============|
# @description: The monitor allows us to view those 
# 				events and tasks that we have done.

# 7. Creating a label that acts as a >> Lower monitor <<
# 		using a "textvar" to modify the label's content
msg_lwm = StringVar()
msg_lwm.set("Welcome to Kai-editor!")
lower_monitor = Label(root, textvar = msg_lwm, justify = "left")
lower_monitor.pack(side = "left")
# |================================================|

# 5. Adding >> menu_bar << to the >> root <<
root.config(menu = menu_bar)

# Finalmente, bucle de la aplicación
root.mainloop()
