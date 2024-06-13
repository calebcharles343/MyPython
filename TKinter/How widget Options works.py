from tkinter import *

# from tkmacosx import * :only for macosx

win = Tk()

win.title('My First Application')
win.wm_geometry('600x400+100-100')

# l = Radiobutton(win, text='Hello World', bg='blue') # bg: background color

'''
# background color

# l = Radiobutton(win, text='Hello World', bg='blue', fg='white') # fg: font color
# OR Dictionary form
l = Radiobutton(win) 
l['text'] = 'Hello world'
l['bg'] = 'blue'
l['fg'] = 'white' # fg: font color
'''

'''
l = Entry(win, width=100)

l['bd'] = 10  # Border depth
l['text'] = 'Hello world'
l['bg'] = 'blue'
l['fg'] = 'white'
l.config(font='Ariel, 20')  # font size
l.pack(pady=100)  # padx and pady for padding

'''

'''
l = Entry(win, width=100)
l['justify'] = 'right'  # means text entry from right side
l['bd'] = 3
l['text'] = 'Hello world'
l['bg'] = 'blue'
l['fg'] = 'white'
l.config(font='Ariel, 20') 
l.pack(pady=100)  

'''

l = Entry(win, textvariable = "var") # to save text in 'var'

l['width'] = 100
l['justify'] = 'right'  # means text entry from right side
l['bd'] = 3
l['text'] = 'Hello world'
l['bg'] = 'blue'
l['fg'] = 'white'
l.config(font='Ariel, 20')
l.pack(pady=100)

win.mainloop()
