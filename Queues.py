# Queues 

#Queues are not implemented ;as queues have a fixed size, and resizing it can be costly; shifting of the entire array once first is removed

#Queues work on the principle of FIFO

class Queue:
    def __init__(self):
        self.l = [] 
    
    def pop(self):
        if len(self.l) == 0:
            return 'Empty'
        else:
            return self.l.pop(0)
    
    def peek(self):
        if len(self.l) == 0:
            return "empty"
        return self.l[0]

    def add(self,x):
        self.l.append(x)
    
    def size(self):
        return len(self.l)


    
        

