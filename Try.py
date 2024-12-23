class Stack(object):
    def __init__(self):  # Initialize the stack
        self.items = []
        
    def push(self, x):  # Push an element onto the stack
        self.items.append(x)
    
    def pop(self):  # Pop the top element (last in the list)
        if not self.items:  # Check for underflow
            print("Underflow")
            return None
        return self.items.pop()

def add_values(l):
    for x in range(1, 5):  
        l.push(x)

def reversestack(l):
    if not l.items: 
        return
    temp = l.pop()  
    reversestack(l)  
    insert_at_bottom(l, temp)  

def insert_at_bottom(l, item):
    if not l.items:  
        l.push(item)
    else:
        temp = l.pop() 
        insert_at_bottom(l, item) 
        l.push(temp)  


l = Stack()
add_values(l)
reversestack(l)
print(l.items)  