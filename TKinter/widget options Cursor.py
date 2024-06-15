from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x600')

# e1 = Text(win, insertbackground='red', insertwidth=15, insertborderwidth=5)
# e1 = Text(win, insertbackground='red', insertwidth=15, insertborderwidth=5, insertontime=1000)  # insertofftime
# e1 = Text(win, cursor='pencil')
e1 = Label(win, text='Label1', cursor='boat')

e1.pack()

win.mainloop()
