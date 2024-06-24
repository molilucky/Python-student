from tkinter import *

root = Tk()

GIRLS = ["xs", "wzjgcfgf", "dc", "ygfgf"]
var = []

for girl in GIRLS:
    var.append(IntVar())
    Checkbutton(root, text=girl, variable=var[-1]).pack(anchor=W)

mainloop()
for i in var:
    print(i)
