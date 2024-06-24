from tkinter import *
import hashlib

root = Tk()

text = Text(root, height=5, width=20)
text.pack()

text.insert(INSERT, "I love FishC.com!")
contents = text.get(1.0, END)


def getSig(contents):
    m = hashlib.md5(contents.encode('utf-8'))
    return m.digest()


sig = getSig(contents)


def check():
    contents = text.get(1.0, END)
    if sig != getSig(contents):
        print("警报：内容发生变动")
    else:
        print("风平浪静")


Button(root, text="检查", command=check).pack()

mainloop()
