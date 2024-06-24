from tkinter import *

root = Tk()

text = Text(root, height=30, width=50)
text.pack()

text.insert(INSERT, "I love fish")
print(text.get(1.2, "1.end"))
mainloop()
