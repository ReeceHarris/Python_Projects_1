from abc import ABC, abstractmethod  # importing abstract method 

class cars(ABC): # defining parent class cars 
   @abstractmethod 
   def movement(self): # defining parent class
      pass
   def handling(self):
      print("Cars and Trucks handle differently") 

class Truck(cars):

   def movement(self): 
      print("A truck goes slow.")

class RaceCar(cars):
   
   def movement(self):
      print("Race cars go fast!")


T = Truck()  # Calling the classes 
T.movement()

R = RaceCar()
R.movement()

T.handling()
R.handling()
