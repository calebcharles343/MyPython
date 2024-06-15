from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400')

# b1 = Button(win, text='Button 1', bd='1m', bg='red', fg='yellow', anchor=W)  # 1c: 1 centimeter (1c, 1i: 1inch, 1m: 1
# millimeter)

b1 = Button(win, text='Button 1', bd='1i', bg='red', fg='yellow', relief=RAISED, overrelief=SUNKEN)  # relief &
# overrelief : FLAT, RAISED, SUNKEN,GROOVE, RIDGE
b2 = Button(win, text='Button 2', )

b1.pack()
b2.pack()

win.mainloop()
