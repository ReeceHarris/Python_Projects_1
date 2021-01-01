import webbrowser 
from tkinter import *

window = Tk() 
windowFrame = Frame(window)
windowFrame.pack() 
window.title("Webpage Generator")
label = Label(windowFrame, anchor = CENTER, text = "This is more content V2") 
label.configure(font = ("helvetica", 14))
label.grid(column = 0, row = 0, pady = 14, padx = 12, sticky = N+W) 
txt = Text(windowFrame, wrap = WORD, width = 30, height = 12)
txt.grid(column = 0, row = 1, padx = 20, pady =20)

def clicked(): 
   usercontent = txt.get('1.0', END)
   
   def webPage(content): 
      f = open("example_site.html", "w")
      f.write("<html><body><h2>{}</h2></body></html>".format(content))
      f.close()
      webbrowser.open("example_site.html")
   webPage(usercontent)

button = Button(windowFrame, anchor = CENTER, text = "Click to create page", command = clicked)
button.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = N)



window.mainloop()

