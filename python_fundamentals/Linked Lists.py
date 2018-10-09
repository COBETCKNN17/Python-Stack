class SLNode:
 def __init__(self, value):
  self.value = value
  self.next = None
  print(self.value)
  return self

class SList:
 def __init__(self):
  self.head = None
  self.tail = None

list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')

########################

class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Slist:
    def __init__(self, value):
        node = Node(value) 
        self.head = node 

def printAllValues(self):
    # whatever self.head is pointing to, I want you to point to where self.head is pointing to  
    runner = self.head 
    while(runner.next != None):
        print(runner.value)
        runner = runner.next 

def addNode(self, value): 
    runner = self.head 
    while(runner.next != None):
        runner = runner.next 
    # now runner points to the last Node 
    node = Node(10)
    runner.next = node 
