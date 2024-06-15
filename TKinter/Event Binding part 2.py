from tkinter import *
from tkinter.messagebox import *  #

# from tkmacosx import * :only for macosx

'''
# Event modifier: specialKey + KeyPress


'''

'''
def event(e):
    print('Event is Generated')
'''


# BINDING MULTIPLE FUNCTION ON WIDGET

def func(e):
    showinfo('Mybox', 'Event is Generated')


def func1(e):
    showinfo('Mybox', e)


win = Tk()

win.title('My First Application')
win.geometry('600x400+100-100')

e = Entry(win, bg='red', fg='yellow')

e.place(x=100, y=100, width=200, height=50)

# e.bind(' <Double - Button-1>', func)  # Double - Button-1 : Event modifier
e.bind('<Button-1>', func)  #
e.bind('<KeyPress>', func1, add='+')  # binding multiple functions on widget ( add='+' )

win.mainloop()
