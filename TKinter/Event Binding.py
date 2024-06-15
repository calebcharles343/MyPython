from tkinter import *
from tkinter.messagebox import *  #

# from tkmacosx import * :only for macosx

'''
Level of Event Binding
1, Instance level binding command 
- For each instance of a widget a bind function is required

2, class level binding
3, application level binding
'''

'''
def event(e):
    print('Event is Generated')
'''


def func(e):
    showinfo('Mybox', 'Event is Generated')


win = Tk()

win.title('My First Application')
win.geometry('600x400+100-100')

e = Entry(win, bg='red', fg='yellow')
e.place(x=100, y=100, width=200, height=50)

e1 = Entry(win, bg='red', fg='yellow')
e1.place(x=100, y=160, width=200, height=50)

# e.bind('<Button-1 >', func)  # Button-1 = left-click, Button-2 = right-click
# e.bind('<Enter>', func)  # onMouseEnter
# e.bind('<Leave>', func)  # onMouseLeave

# e.bind('<KeyPress>', func)  # onKeyPress (INSTANCE LEVEL BINDING: func affects only the widget mentioned e. )

# win.bind_class('Entry', '<Button-1>', func)  # onKeyPress (CLASS LEVEL BINDING: func affects
# all widgets instance e and e1

win.bind_all('<Button-1>', func)  # onKeyPress (APPLICATION LEVEL BINDING: func affects the entire window

win.mainloop()
