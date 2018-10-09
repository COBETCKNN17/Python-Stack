def randInt(min=0, max=100):
    return random.randrange(min,max)  

print(randInt()) 
print(randInt(0,max=50))
print(randInt(min=50))
print(randInt(min=50, max=500)) 
