from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=42, tickinterval=5, length=200, resolution=5, orient=VERTICAL)
s1.pack()
s2 = Scale(root, from_=0, to=200, tickinterval=10, length=600, resolution=5, orient=HORIZONTAL)
s2.pack()


def show():
    print(s1.get(), s2.get())


Button(root, text="获取位置", command=show).pack()
mainloop()
