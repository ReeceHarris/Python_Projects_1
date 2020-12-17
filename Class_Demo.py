
def __init__(Soldier, name, rank, ID):
    Soldier.name = name
    Soldier.rank = rank
    Soldier.ID = ID 




class Soldier:
    name = 'Smith'
    rank = 'spc'
    ID = '12345'

class airborne(Soldier):
    jumps = '12'
    qualified = True


class MOS(Soldier):
    MOSQ = True
    Job = '11B' 
