from tkinter import *

root = Tk()

text1 = Text(root, height=30, width=50)
text1.pack()
text1.insert(INSERT, 'I love Fish')
text1.mark_set("here", '1.2')
text1.insert("here", "插")
text1.insert("here", "入")

text2 = Text(root, height=30, width=50)
text2.pack()
text2.insert(INSERT, 'I love Fish')
text2.mark_set("here", '1.2')
text2.mark_gravity("here", LEFT)
text2.insert("here", "插")
text2.insert("here", "入")
mainloop()
