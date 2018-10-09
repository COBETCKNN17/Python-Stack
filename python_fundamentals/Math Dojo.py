'''
Practice creating a class and creating new instances
Practice chaining methods
Practice writing flexible functions that can take a variable number of arguments
'''

class MathDojo: 
    def __init__(self): 
        self.total = 0
    def add(self, x=0, y=0): # defaulting parameters to 0
        self.total = self.total + x + y 
        print("After addition, the current total is", self.total)
        return self 
    def subtract(self, u=0, z=0): 
        self.total = self.total - u - z
        print("After subtraction, the current total is", self.total)
        return self 

z = MathDojo.add(3) 
z.add(3).add(3).add(9).subtract(323)


class MathDojo: 
    def __init__(self): 
        self.total = 0
    def add(self, x, *vals): 
        for i in vals:
            x += i
        self.result = x 
        print("After addition, the current total is", self.result)
        return self 
    def subtract(self, u=0, z=0): 
        self.total = self.total - u - z
        print("After subtraction, the current total is", self.total)
        return self 