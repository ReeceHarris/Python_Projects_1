class Protected:      #Example class
   def __init__(self): 
      self.__privateAttribute = 1  # 2 underlines indicate the attribute is private and should not be changed
      self._privateAttribute = 2  # 1 underline indicates it is a protected class 
         
      obj = Protected() # obj using protected class to retrieve private and protected arguments 
      obj.get_privateAttribute() 
      obj.get__privateAttribute() 

      
      print(obj)





