# Queues 

#Queues are not implemented ;as queues have a fixed size, and resizing it can be costly; shifting of the entire array once first is removed

class Queue:
    def __init__(self):
        self.l = [] 
    
    def pop(self,l):
        if l == []:
            return 'Empty'
        else:
            return l.pop(0)
        

