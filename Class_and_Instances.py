class Candy():
    base = 'Unknown'
    filler = 'Unknown'
    center = 'Unknown'
    topping = 'Unknown'
    shape = 'Unknown'

    def information(self):
        msg = "\nbase: {}\nfiller: {}\ncenter: {}\ntopping: {}\nshape: {}".format(self.base, self.filler, self.center, self.topping, self.shape)
        print(msg) 



class Snickers(Candy):
    base = 'nougat'
    filler = 'caramel'
    center = 'peanuts'
    topping = 'chocolate'
    shape = 'bar'
    def slogan(self):
        msg = "\nYour not you when your hungry!"
        print(msg) 
    

class KitKat(Candy):
    base = 'waffers'
    filler = 'chocolate'
    center = 'waffers'
    shape = 'bars'

    def snap(self):
        msg = '\nsnap snap crunch!'
        print(msg) 


    
def __init__(base, filler, center, topping, shape):
    #Snickers = slogan()
    print(Snickers.information())
    print(Snickers.slogan())

    KitKat = snap()
    print(KitKat.information())
    print(KitKat.snap)


snickers = Snickers()
snickers.information()



    
