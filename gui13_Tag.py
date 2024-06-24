from tkinter import *
import webbrowser

root = Tk()

text = Text(root, height=5, width=30)
text.pack()

text.insert(INSERT, "I love FishC.com")
text.tag_add("link", "1.7", "1.16")


def show_hand_cursor(event):
    text.tag_config("link", foreground="blue", underline=True)
    text.config(cursor="arrow")


def show_arrow_cursor(event):
    text.tag_config("link", foreground="", underline=False)
    text.config(cursor="xterm")


def click(event):
    webbrowser.open("http://www.fishc.com")


text.tag_bind("link", "<Enter>", show_hand_cursor)
text.tag_bind("link", "<Leave>", show_arrow_cursor)
text.tag_bind("link", "<Button-1>", click)

mainloop()
