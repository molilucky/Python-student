from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

line1 = w.create_line(0, 0, 200, 100, fill='green', width=3)
line2 = w.create_line(200, 0, 0, 100, fill='green', width=3)
rec1 = w.create_rectangle(40, 20, 160, 80, fill='blue')
rec2 = w.create_rectangle(65, 35, 135, 65, fill='yellow')

w.create_text(100, 50, text='World')

w2 = Canvas(root, width=200, height=100)
w2.pack()
rec3 = w2.create_rectangle(40, 20, 160, 80, dash=(4, 4))
oval = w2.create_oval(40, 20, 160, 80, fill='pink')
w2.create_text(100, 50, text="Fish")

mainloop()
