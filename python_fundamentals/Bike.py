class Bike: 
    def __init__(self, price, max_speed, miles): 
        self.price = 500 
        self.max_speed = "35mph"
        self.miles = 0
    def displayInfo(self): 
        print("This bike's price is", self.price)
        print("This bike's max speed is", self.max_speed) 
        print("This bike's has {} total miles riden on it.".format(self.miles))
        return self
    def ride(self): 
        print("Riding...")
        self.miles = self.miles + 10 
        return self
    def reverse(self):
        print("Reversing...")
        self.miles = self.miles - 10 
        return self
     
# Creating first instance of Bike 
Trek = Bike(310, "32mph", 3)
Trek.ride()
Trek.ride()
Trek.ride() 
Trek.reverse()
Trek.displayInfo() 

# Creating second instance of bike 
Specialized = Bike(300, "35mph", 4)
Specialized.ride() 
Specialized.ride() 
Specialized.reverse()
Specialized.reverse()
Specialized.displayInfo()

# Creating third instsance of Bike 
Schwinn = Bike(150, "20mph", 0)
Schwinn.reverse() 
Schwinn.reverse() 
Schwinn.reverse() 
Schwinn.displayInfo() 