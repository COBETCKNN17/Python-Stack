class Animal:
    def __init__(self, name, health): 
        self.name = name 
        self.health = health 
    def walk(self): 
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self 
    def display_health(self): 
        print("The {}'s health is {}".format(self.name, self.health)) 
        return self 

Gorilla = Animal("Gorilla", 20)
Gorilla.walk().walk().walk().run().run().display_health() 

class Dog(Animal): 
    def __init__c(health=150):
        return self 
    def pet_the_dog(self): 
        self.health = self.health + 5
        print("The dog's health is", self.health)
        return self 

ooog = Dog("ooog", 140)
Dog.walk().walk().walk().run().run().pet_the_dog().display_health() 
    
class Dragon(Animal):
    def __init__c(health=170): 
        return self 
    def fly(self): 
        self.health = self.health - 10
        return self 
    def display_health(self):
        print(Animal.display_health(self), "\nI am a dragon!") 
        return self 

drag = Dragon("drag", 180)
drag.display_health()