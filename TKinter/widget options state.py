from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400')

# b1 = Entry(win, highlightbackground='red', highlightthickness=5, highlightcolor='yellow')

# b1 = Button(win, text='Button 1', state='disabled')  # state:  active, disabled, or normal

# b1 = Button(win, text='Button 1', state='active',activebackground='red', activeforeground='yellow')

# b1 = Button(win, text='Button 1', state='disabled',disabledforeground='red')

# b2 = Button(win, text='Button 2', takefocus=0)  # takefocus = 0: no focus on button

b1 = Listbox(win, activestyle=UNDERLINE)  # activestyle: DOTBOX, UNDERLINE
b1.insert(0, 'a')
b1.insert(1, 'b')
b1.insert(2, 'c')
b1.insert(3, 'd')

b2 = Checkbutton(win, text='Button 2', indicatoron=False)  # indicatoron=False: remove mark box


b1.pack()
b2.pack()

win.mainloop()