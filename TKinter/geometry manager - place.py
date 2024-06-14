from tkinter import *

# from tkmacosx import * :only for macosx

# ####### PLACE #######

win = Tk()

win.title('My First Application')
win.wm_geometry('600x400+100-100')  # This is just for positioning for my screen work space

b1 = Button(win, text='Label 1', bg='lightblue', fg='blue')
b2 = Button(win, text='Label 2', bg='lightblue', fg='blue')

# b1.place(x=100, y=100, width=150, height=100)  # x and y for absolute placement
# b2.place(x=250, y=200, width=150, height=100)

# Or

b1.place(relx=0.5, rely=0.5, relwidth=0.20, relheight=0.10)  # relx and rely for relative placement
# b2.place(x=250, y=200, width=150, height=100)

win.mainloop()