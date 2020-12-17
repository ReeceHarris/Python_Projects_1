
def __init__(Soldier, name, rank, ID): #Defines new object
    Soldier.name = name  #Initial Attributes 
    Soldier.rank = rank
    Soldier.ID = ID 



class Soldier:    # Main class being made 
    name = 'Smith' 
    rank = 'spc'
    ID = '12345'

class airborne(Soldier): #Child class of Soldier 
    jumps = '12'  #Added attribute 
    qualified = True


class MOS(Soldier):  # Chile od class Soldier 
    MOSQ = True  #Added Attribute 
    Job = '11B' 
