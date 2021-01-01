import webbrowser    #Import webbrowser module for more functionality 
from tkinter import * #import Tkinter for gui creation and costumization 

window = Tk() # sets value for window to Tkinter variable 
windowFrame = Frame(window)
windowFrame.pack() # Forces all buttons and windows to be packed together 
window.title("Webpage Generator") # title for the program 
label = Label(windowFrame, anchor = CENTER, text = "This is more content V2") 
label.configure(font = ("helvetica", 14)) # styling for label 
label.grid(column = 0, row = 0, pady = 14, padx = 12, sticky = N+W) # styling and positioning for label
txt = Text(windowFrame, wrap = WORD, width = 30, height = 12) 
txt.grid(column = 0, row = 1, padx = 20, pady =20)

def clicked(): # function clicked will be called when button click to create page is clicked
   usercontent = txt.get('1.0', END)
   
   def webPage(content): # Function webPage creates the basic website 
      f = open("example_site.html", "w")
      f.write("<html><body><h2>{}</h2></body></html>".format(content)) #format method inserts the added string inputed by the user 
      f.close()
      webbrowser.open("example_site.html") # Opens the website into the web browser 
   webPage(usercontent) # calls webPage from within function clicked 

button = Button(windowFrame, anchor = CENTER, text = "Click to create page", command = clicked) # button to call function webPage 
button.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = N) # button styling 



window.mainloop()  # Keeps the gui open till dismissed 

