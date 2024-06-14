from tkinter import *

# from tkmacosx import * :only for macosx

'''
# Event Handling:
-
'''


def fun(msg):
    print(msg)


win = Tk()

win.title('My First Application')
win.wm_geometry('600x400+100-100')

# b1 = Button(win, text='My Button', command=fun)  # event handler binding
b1 = Button(win, text='My Button', command=lambda: fun('Button is clicked'))  # event handler binding with perimeter
b1.pack()

win.mainloop()
