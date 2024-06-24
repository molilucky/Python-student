import tkinter as tk
from tkinter import *

root = Tk()

# textLabel = Label(root, text="Hello World")
# textLabel.pack(side=LEFT)
# photo = PhotoImage(file='cat.gif')
# imgLabel = Label(root, image=photo)
# imgLabel.pack(side=RIGHT)

Photo = PhotoImage(file="cat.gif")
theLabel = Label(root,
                 text="活到老\n学到老",
                 justify=CENTER,
                 image=Photo,
                 compound=CENTER,
                 font=("华康少女字体", 20),
                 fg="white"
                 )
theLabel.pack()
mainloop()
