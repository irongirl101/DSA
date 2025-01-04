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

q = Queue()

for i in range(5):
    q.add(i)

#print(q.l) -> method to print 

print(q.pop())
print(q.peek())
print(q.size())
    
#Queue implementation using linked lists 

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None 
        self.length = None 
    
    def enqueue(self,x):
        node = Node(x)
        if self.rear == None:
            self.front = self.rear = node 
            self.length+=1 
            return
        self.rear.next = node 
        self.rear = node 
        self.length+=1 
    
    def dequeue(self):
        if self.length == 0:
            return "empty"
        
        temp = self.front 
        self.front = temp.next 
        self.length-=1
        if self.front== None:
            self.rear = None 
        return temp.data 
    
    def peek(self):
        if self.length == 0:
            return "empty"
        else:
            return self.front.data

    def size(self):
        return self.length
    
    def displayqueue(self):
        temp = self.front 
        while temp:
            print(temp.data,end='')
            temp = temp.next 
        print()

l = Queue()

l.enqueue(1)
l.enqueue(2)
l.enqueue(3)
l.displayqueue()



    
        

        

