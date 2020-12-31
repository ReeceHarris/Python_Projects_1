import webbrowser 
import tkinter 





f = open("demofile2.html", "a")
f.write("{}"),format(addedText)
addedText = "" 
f.close()

#open and read the file after the appending:
f = open("demofile2.html", "r")
print(f.read())

webbrowser.open_new_tab("demofile2.html")

