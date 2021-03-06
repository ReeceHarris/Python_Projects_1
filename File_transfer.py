# list of imported modules for additional functionality 
import shutil 
import os 
import tkinter as tk 
import os.path,time 
from tkinter import * 
from tkinter import filedialog 
from datetime import * 


# creating a class to organize and have 
class windowTk(Frame): 
   def __init__(self, master, *args, **kwargs): 
      Frame.__init__(self, master, *args, **kwargs)
      self.master = master 
      self.master.minsize(600, 400)   # gui size 
      self.master.maxsize(900, 750)
      self.master.title("File Transfer")  #gui title
      self.label_1 = tk.Entry(self.master)
      self.label_1.grid(row=0, columnspan= 5)
      self.button1 = Button(text = "source", command = self.button_1) # creates source button and calls function button_1 
      self.button1.grid(row = 0, column = 8)
      self.label_2 = tk.Entry(self.master)
      self.label_2.grid(row=2, columnspan= 5)
      self.button2 = Button(text = "destination", command = self.button_2)# creates source button and calls function button_2 
      self.button2.grid(row=2, column= 8)
      self.button3 = Button(self.master, text = "Run", command = self.File_Transfer)# creates source button and calls function File_Transfer 
      self.button3.grid(row = 4, column = 4)

      
   def button_1(self): #Opens directory window for file selection 
      filename = filedialog.askdirectory() 
      self.label_1.insert(0,filename)

   def button_2(self):  #Opens directory window for file selection 
      filename2 = filedialog.askdirectory()
      self.label_2.insert(0,filename2)

   def File_Transfer(self): #Uses the 2 directories given from button_1 and 2 var filename and filename2 
      source = self.label_1.get()
      destination = self.label_2.get() 
      files = os.listdir(source)

      for i in files: # Checks last modified time and has an established limit of 1 day 
         modifytime = os.path.getmtime(source + "/" + i)
         modifydate = datetime.fromtimestamp(modifytime)
         todaysdate = datetime.today() 
         limit = todaysdate - timedelta(days=1)

         if modifydate > limit: # if it is within the limit will send a copy from source to destination 
            shutil.copy(source + "/" + i, destination) 


if __name__== "__main__": # dundder method for keeping the gui open while the code runs 
   root = tk.Tk() 
   app = windowTk(root)