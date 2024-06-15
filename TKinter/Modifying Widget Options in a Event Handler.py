from tkinter import *
from tkinter.messagebox import *

# from tkmacosx import * : only for macosx
'''
def my_handler1(e):
    print(lbl.cget('text'))
    # showinfo('My Info', lbl.cget('text'))
    showinfo('My Info', lbl.cget('bg'))
    # lbl.config(bg='red')
    lbl['bg'] = 'red'
'''

'''
# Using two separate event_handlers
def my_handler1(e):
    lbl['bg'] = 'blue'
    lbl['text'] = 'Blue Color'


def my_handler2(e):
    lbl['bg'] = 'red'
    lbl['text'] = 'Red Color'
'''


# Combining event_handlers 1 - 2 using Event type order number
def my_handler(e):
    if int(e.type) == 7:  # Event type order number (always convert e.type to integer)
        lbl['bg'] = 'blue'
        lbl['text'] = 'Blue Color'

    elif int(e.type) == 8:  # Event type order number
        lbl['bg'] = 'red'
        lbl['text'] = 'Red Color'
 

win = Tk()
win.title('My First Application')
win.geometry('600x400')

lbl = Label(win, text='blue color', bg='blue', fg='white', width=20, height=2)
lbl.pack()
# lbl.bind('<Button-1>', my_handler1)

# lbl.bind('<Enter>', my_handler2)
# lbl.bind('<Leave>', my_handler1)
lbl.bind('<Leave>', my_handler)

win.mainloop()
