from tkinter import *
import webbrowser

root = Tk()

Label(root, text="在下面输入网址").grid(row=1)
v = StringVar()
e = Entry(root)
e.grid(row=2)



def click(e=e):
    webbrowser.open(e.get())


Button(root, text="点击查询", command=click).grid(row=3)
mainloop()
