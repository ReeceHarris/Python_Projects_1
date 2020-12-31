class Protected:      #Example class
   def __init__(self): 
      self.__privateAttribute = 1  # 2 underlines indicate the attribute is private and should not be changed
      self._privateAttribute = 2  # 1 underline indicates it is a protected class
      
   def GetAtt(self):
      print(self.__privateAttribute)




obj = Protected() # obj using protected class to retrieve private and protected arguments 
obj.__privateAttribute = 5 
obj.GetAtt()



print(obj.__privateAttribute)





