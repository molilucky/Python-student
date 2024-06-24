from tkinter import *

root = Tk()

text = Text(root, width=30, height=5, undo=True, autoseparators=False, maxundo=10)
text.pack()


def callback(event):
    text.edit_separator()


text.bind('<Key>', callback)

text.insert(INSERT, "I love FishC")


def show():
    text.edit_undo()


def show1():
    text.edit_redo()


Button(root, text="撤销", command=show).pack()
Button(root, text="恢复", command=show1).pack()

mainloop()
