from tkinter import *
from tkinter.messagebox import * #

# from tkmacosx import * :only for macosx

'''
Level of Event Binding
1, Instance level binding command
2, class level binding
3, application level binding
'''


'''
def event(e):
    print('Event is Generated')
'''

def event(e):
    showinfo('Mybox','Event is Generated')


win = Tk()

win.title('My First Application')
win.wm_geometry('600x400+100-100')

e = Entry(win, bg='red', fg='yellow')

e.place(x=100, y=100, width=200, height=50)

# e.bind('<Button-1 >', event)  # Button-1 = left-click, Button-2 = right-click
# e.bind('<Enter>', event)  # onMouseEnter
# e.bind('<Leave>', event)  # onMouseLeave
e.bind('<KeyPress>', event)  # onKeyPress

win.mainloop()
