''' Provided Code '''
# step 1 create node constructor 
class Node(self, value): 
    self.value = value 
    self.next = None

# step 2 create Single Linked List
class SList: 
    def __init__(self,value):
        node = Node(value)
        self.head = node # making the head of the created list point to the recently created node 
    def addNode(self, value):
        node = Node(value) 
        runner = self.head # initialize runner at the head element 
        while(runner.next != None):
            runner = runner.next
        runner.next = node # at the end of the loop, assign runner.next to look at the most recent node 
    def removeNode(self, value):
        if self.head != None: 
            current = self.head 
        if self.head.next == None: 
            self.head = None 
            while current.next != None: 
                current = current.next 
                if current.next.next == None: # only element in the list 
                    current.next = None 
        else: 
            print("No nodes")
            return False 
    def printAllValues(self, msg=""):
        runner = self.head 
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next)) 
            runner = runner.next 
        print(id(runner), runner.value, id(runner.next)) 
      
print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9)
list.printAllValues("Attempt 1")
''' ''' 

