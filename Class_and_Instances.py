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
    def __init__(self):
        #Snickers = slogan()
#        print(Snickers.information())
 #       print(Snickers.slogan())

        self.base = 'nougat'
        self.filler = 'caramel'
        self.center = 'peanuts'
        self.topping = 'chocolate'
        self.shape = 'bar'
        self.label = 'brown'
        self.allergies = 'nuts' 
    def information(self):
        self.msg = "\nYour not you when your hungry!"
        print(self.msg) 
    

class KitKat(Candy):
    base = 'wafers'
    filler = 'chocolate'
    center = 'wafers'
    shape = 'bars'
    parts = '4'
    taste = 'chocolatey' 

    def information(self):
        msg = '\nsnap snap crunch!'
        print(msg) 


Snickers_test = Snickers()
Snickers_test.information()

#print(Snickers_test.base) 

##    
##def __init__(base, filler, center, topping, shape):
##    #Snickers = slogan()
##    print(Snickers.information())
##    print(Snickers.slogan())
##
##    KitKat = snap()
##    print(KitKat.information())
##    print(KitKat.snap)


snickers = Snickers()
snickers.information() #prints info specified in information

kitkat = KitKat()
kitkat.information()








    
