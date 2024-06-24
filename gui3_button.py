from tkinter import *


def callback():
    var.set("我才不信")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("你是甲鱼吗")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack()

photo = PhotoImage(file='cat.gif')
imgLabel = Label(frame1, image=photo)
imgLabel.pack()

theButton = Button(frame2, text='我是甲鱼', command=callback)
theButton.pack()

frame1.pack()
frame2.pack()

mainloop()
