from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

entry = Entry(frame)
entry.pack(side = 'right') 

label = Label(frame, text = 'Nombre:')
label.pack(side = 'left')

frame2 = Frame(root)
frame2.pack()

entry2 = Entry(frame2)
entry2.pack(side = 'right') 

label2 = Label(frame2, text = 'Apellido')
label2.pack(side = 'left')



root.mainloop()