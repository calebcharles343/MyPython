from tkinter import *

win = Tk()

win.title('My First Application')
win.wm_geometry('600x400+100-100')

'''
# label
l = Label(win, text='Hello World')  # create a text label
l.pack()  # to add label to window
'''

'''
# button
b = Button(win, text='Click Me')
b.pack()
'''

'''
# entry

# label
l = Label(win, text='Name')  # create a text label
l.pack()  # to add label to window


e = Entry(win)
e.pack()
'''

'''
# text multiple lines
t = Text(win, width=30, height=10)
t.pack()
'''

'''
# Check Button
checkBtn = Checkbutton(win, text='yes ')
checkBtn.pack()
'''

'''
# Radio Button
checkBtn1 = Radiobutton(win, text='Option1', variable='v1', value=1)
checkBtn1.pack()

checkBtn2 = Radiobutton(win, text='Option2', variable='v1', value=2)
checkBtn2.pack()

checkBtn3 = Radiobutton(win, text='Option3', variable='v1', value=3)
checkBtn3.pack()
# Note make a group with same variable='value' like this so only one can be selected
'''

'''
# Option menu
v = StringVar()
optionMenu = OptionMenu(win, v, 'python', *('Java','C++','Python', 'JavaScript'))
optionMenu.pack()
'''

# Scale
scl = Scale(win, from_=0, to=100)
scl.pack()

win.mainloop()
