# Python Ver: 3.8.5
#
# Author: Reece Harris 
#
# Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#          using Tkinter Parent and Chile relationships 
#
# Tested OS: This code was written and tested to work with Windows 10


from tkinter import *
import tkinter as tk



# Be sure to import out other modules
# so we can have access to them
import phonebook_student_gui
import phonebook_student_func



# Frame is the from the Tkinter class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        #define our master frame configuration
        self.master = master
        self.master.minsize(500,450) #(Height, Width)
        self.master.maxsize(500,450)
        # This CenterWindow method will center our app on the user's screen
        phonebook_student_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#aaa1bd")
        #This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper coner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_student_func.ask_quit(self))

        # load in the gui widgets from a seperate module,
        # keeping your code comparmentalized and clutter free
        phonebook_student_gui.load_gui(self) 


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
