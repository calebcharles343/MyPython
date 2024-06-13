from tkinter import *

win = Tk()  # to create a window

win.title('My First Application')  # To name the window

# win.wm_geometry('600x400+100+100')  # for window size : 600x400 margin(x and y):+100+100
# win.wm_geometry('600x400-100-100')  # for window size : 600x400 margin(x and y):+100+100
win.wm_geometry('600x400+100-100')  # for window size : 600x400 margin(x and y):+100+100
win.resizable(False, True)  # resize only on y:axis

win.attributes('-alpha', 0.50 )  # to change opacity or transparency

win.mainloop()  # to run the window
