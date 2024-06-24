from tkinter import *

root = Tk()

group = LabelFrame(root, text="最好的脚本语言是？", padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [
    ('python', 1),
    ('java', 2),
    ('javascript', 3),
    ('ruby', 4),
]

v = IntVar()
v.set(1)
for lang, numbers in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=numbers)
    b.pack(anchor=W)
mainloop()
