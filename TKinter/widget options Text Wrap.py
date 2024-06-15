from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400')

# e1 = Text(win, wrap=WORD)  # spacing1 and spacing2
e1 = Label(win, text='aaaaaaaaaaaaaaambcbbbbcbcnn', width=100, wraplength=100)


e1.pack()

win.mainloop()
