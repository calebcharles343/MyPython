from tkinter import *

# from tkmacosx import * :only for macosx


'''
 Geometry manager : helps us manage layout screen
 Types:
 - pack
 - grid
 - place 
'''
# ####### PACK #######
win = Tk()

win.title('My First Application')
win.wm_geometry('+100-100')

'''
#SIDE
l1 = Label(win, text='Label 1', bg='red', fg='yellow')
l1.pack(side=LEFT)  # using side

l2 = Label(win, text='Label 2', bg='red', fg='yellow')
l2.pack(side=TOP)

l3 = Label(win, text='Label 3', bg='red', fg='yellow')
l3.pack(side=RIGHT)
'''

'''
#ANCHOR
l1 = Label(win, text='Label 1', bg='red', fg='yellow')
l1.pack(anchor=NW)  # using anchor: north_west
# note: anchor is base on the arrangement of widget line
l2 = Label(win, text='Label 2', bg='red', fg='yellow')
l2.pack(anchor=SE)  # south_east

l3 = Label(win, text='Label 3', bg='red', fg='yellow')
l3.pack(anchor=S)  # north_east
'''

'''
#PADDING
l1 = Label(win, text='Label 1', bg='red', fg='yellow')
l1.pack(padx=2, pady=2, ipady=50)  # padx and pady for out padding

l2 = Label(win, text='Label 2', bg='red', fg='yellow')
l2.pack(padx=2, pady=2, ipadx=50) # ipadx and ipady for inner padding

l3 = Label(win, text='Label 3', bg='red', fg='yellow')
l3.pack(padx=2, pady=2,  ipady=5)
'''

l1 = Label(win, text='Label 1', bg='red', fg='yellow')
l1.pack(side=LEFT, fill=Y, padx=2, pady=2, ipadx=15, ipady=15)  #

l2 = Label(win, text='Label 2', bg='red', fg='yellow')
l2.pack(side=TOP, fill=X, padx=2, pady=2, ipadx=5, ipady=5)  #

l3 = Label(win, text='Label 3', bg='red', fg='yellow')
l3.pack(side=LEFT, padx=2, pady=2,  ipadx=5, ipady=5)

l4 = Label(win, text='Label 4', bg='red', fg='yellow')
l4.pack(side=LEFT, padx=2, pady=2,  ipadx=5, ipady=5)

win.mainloop()
