from tkinter import *

root = Tk()

theLB = Listbox(root, setgrid=True)
theLB.pack()

for item in ["甲", "乙", "丙", "丁"]:
    theLB.insert(END, item)

Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE)).pack(side=LEFT)
Button(root, text="删除全部", command=lambda x=theLB: x.delete(0, END)).pack(side=RIGHT)

mainloop()
