class Product: 
    def __init__(self, price, item_name, weight, brand, status): 
        self.price = price
        self.item_name = item_name
        self.weight = weight 
        self.brand = brand
        self.status = "for sale"
    def sell(self, price, tax = 0): 
        self.status = "sold"
        return self.status  
    def add_tax(self, price, tax): 
        return self.price * (1 + tax)
    def return_item(self, reason_for_return):
        if reason_for_return == "defective": 
            self.status = "defective"
        elif reason_for_return == "like new": 
            self.status = "for sale"
        elif reason_for_return == "opened":  
            self.status = "used"
            self.price = self.price * (1 - 0.2) # applying 20% discount
        return self
    def displayInfo(self):
        print("This product's name is", self.item_name) 
        print("This product's price is", self.price)
        print("This product's brand is", self.brand)
        print("This product's weight is", self.weight)
        print("This product's status is", self.status)
        return self 

Computer = Product(1000, "MacBook Pro", "1 lb", "Apple", "for sale")
Computer.return_item("defective")
Computer.return_item("opened")
Computer.add_tax(2000, 0.14)
Computer.sell(1900)
