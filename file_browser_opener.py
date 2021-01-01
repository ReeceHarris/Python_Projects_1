# Python program to create 
# a file explorer in Tkinter 
import webbrowser 
# import all components 
# from the tkinter library 
from tkinter import *

# import filedialog module 
from tkinter import filedialog 

# Function for opening the 
# file explorer window
filename = "demofile2.html"
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/Desktop", 
    title = "Select a File", filetypes = (("Htlm files", "*.html*"),("all files", "*.*"))) 
	
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename)
    
Path = filename 
        
	
	
																								
# Create the root window 
window = Tk() 

# Set window title 
window.title('Select a File') 

# Set window size 
window.geometry("500x500") 

#Set window background color 
window.config(background = "grey") 

# Create a File Explorer label 
label_file_explorer = Label(window, 
    text = "File Explorer using Tkinter", 
    width = 100, height = 4, 
    fg = "blue") 

	
button_explore = Button(window, 
    text = "Browse Files", 
    command = browseFiles) 

button_exit = Button(window, 
    text = "Exit", 
    command = exit)


button_launch = Button(window,
    text = "Launch",
    command = lambda:webbrowser.open(Path))
    

            

# Grid method is chosen for placing 
# the widgets at respective positions 
# in a table like structure by 
# specifying rows and columns
                       
label_file_explorer.grid(column = 1, row = 1) 

button_explore.grid(column = 1, row = 2) 

button_exit.grid(column = 1,row = 3)

button_launch.grid(column = 1, row = 4) 

# Let the window wait for any events 
window.mainloop() 
