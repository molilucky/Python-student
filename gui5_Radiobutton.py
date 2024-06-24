from tkinter import *

root = Tk()

v = IntVar()
# Radiobutton(root, text='one', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='two', variable=v, value=2).pack(anchor=W)
# Radiobutton(root, text='three', variable=v, value=3).pack(anchor=W)

LANGS = [("one", 1), ("two", 2), ("three", 3)]

for lang, number in LANGS:
    Radiobutton(root, text=lang, variable=v, value=number).pack()
mainloop()
print(v.get())
