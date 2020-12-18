
 
import sqlite3   # Imports sqlite3 for additional functionality 

connect = sqlite3.connect('test2.db')

with connect:
    A = connect.cursor() # creates new DB with 2 fields 1 integer 1 string
##    print(A)
##    print(type(A))
    A.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        File_list TEXT)") #Creates tbl_persons with 2 columns 1 ID 1 Text 
    connect.commit()
connect.close() #Disconnect from test2.db 

connect = sqlite3.connect('test2.db') # Connects to test2.db

with connect:
    A = connect.cursor() #Connecting with DB and adding strings

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg') #Tuple of values

print(fileList)
print(type(fileList))
for x in fileList:
##    print(x)
##    print(type(x))
    if x.endswith('.txt'): #Condition for file filtering
        with connect: # While loop for searching
            A = connect.cursor()
            A.execute("INSERT INTO tbl_persons (File_list) VALUES (?)", (x,))
            print(x) # Print results 


connect.close()  # Disconnect from test2.db





