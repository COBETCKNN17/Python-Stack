class Car: 
    def __init__(self, price, speed, fuel_economy, mileage): 
        self.price = price
        self.speed = speed 
        self.fuel_economy = fuel_economy 
        self.mileage = mileage 
        if price > 10000: 
            self.tax = 0.15
        else: 
            self.tax = 0.12
        self.displayAll() 
    def displayAll(self): 
        print("This car's price is", self.price)
        print("This car's max speed is", self.speed) 
        print("This car's fuel economy is {} miles per hour.".format(self.fuel_economy)) 
        print("This car's has {} total miles riden on it.".format(self.mileage))
        print("This car's tax is", self.tax) 
        return self
    