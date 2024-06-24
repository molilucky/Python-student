from tkinter import *

root = Tk()

text = Text(root, width=80, height=50)
text.pack()

text.insert(INSERT, "Hello World!")

photo = PhotoImage(file="cat.gif")


def show():
    text.image_create(END, image=photo)


b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()
