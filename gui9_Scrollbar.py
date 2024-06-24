from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

theLB = Listbox(root, setgrid=True, height=20, yscrollcommand=sb.set)
theLB.pack(side=LEFT, fill=BOTH)

for i in range(101):
    theLB.insert(END, i)

sb.config(command=theLB.yview)
mainloop()

