from tkinter import *
from tkinter.messagebox import *


# from tkmacosx import * : only for macosx

def my_handler(e):
    print(e)
    print(e.state)
    print(e.x_root, e.y_root)
    print(e.keysym)
    print(e.keysym_num)
    print(e.char)
    print(e.type)


win = Tk()
win.title('My First Application')
win.geometry('600x400')

ent = Entry(win)
ent.pack()

ent.bind('<Button-1>', my_handler)

win.mainloop()
