Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.pack()
>>> b2.pack()
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b1.pack(side=LEFT, padx = 10)
>>> b2.pack(side=LEFT, padx = 10)
>>> b3 = Button(win, text="3")
>>> b3.pack(side=RIGHT)
>>> b3.pack(side = RIGHT, pady=20)
>>> 