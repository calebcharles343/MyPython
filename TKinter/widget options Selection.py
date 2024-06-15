from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x600')


# e1 = Entry(win, selectbackground='yellow', selectforeground='red')
e1 = Text(win, selectbackground='yellow', selectforeground='red')
lst1 = Listbox(win,  selectbackground='yellow', selectforeground='red', exportselection=False)  # exportselection
lst1.insert(0, 'AAAA')
lst1.insert(1, 'BBBB')
lst1.insert(2, 'CCCC')
lst1.insert(3, 'DDDD')


e1.pack()
lst1.pack()

win.mainloop()
