import tkinter as tk
from tkinter import *


# root = tk.Tk()
# root.title("FishC Demo")
#
# theLabel = tk.Label(root, text="我的第二个窗口程序！")
# theLabel.pack()
#
# root.mainloop()

class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()
        textLabel = Label(frame, text="Hello World")
        textLabel.pack()
        photo = PhotoImage(file='cat.gif')
        imgLabel = Label(frame, image=photo)
        imgLabel.pack()
        # self.hi_there = tk.Button(frame, text="打招呼", fg="red", bg="black", command=self.say_hi)
        # self.hi_there.pack()

    def say_hi(self):
        print("大家好，我是鱼")


root = Tk()
app = App(root)
mainloop()
