#linked lists and a few ops

#Singly Linked List 

def singlylinkedlist():
    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None 

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2 
    node2.next = node3 
    node3.next = node4

    currentnode = node1 
    while currentnode:
        print(currentnode.data)
        currentnode= currentnode.next 
    print("null")

#Doubly Linked List 

def doublyLinkedlist():
    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None
            self.prev = None 
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2 

    node2.next = node3 
    node2.prev = node1 

    node3.next = node4 
    node3.prev = node2 

    node4.prev = node3 

    currentnode = node1
    while currentnode:
        print(currentnode.data)
        currentnode= currentnode.next 
    print("Null")
    currentnode = node4 
    while currentnode:
        print(currentnode.data)
        currentnode=currentnode.prev 
    print("Null")

#circular linked list 
def circularlinkedlist():
    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None 
            
        
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2 
    node2.next = node3 
    node3.next = node4 
    node4.next = node1 

    currentnode = node1 
    startnode = node1 
    print(currentnode.data)
    currentnode=currentnode.next
    while currentnode!=startnode:
        print(currentnode.data)
        currentnode=currentnode.next 
    print("null")

#Circular Doubly Linked List 
def circulardoublylinkedlist():
    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None
            self.prev = None 


    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2 
    node1.prev = node4 

    node2.next = node3 
    node2.prev = node1 

    node3.next = node4 
    node3.prev = node2 

    node4.next = node1 
    node4.prev = node3 

    currentnode = node1 
    startnode = node1 
    print(currentnode.data)
    currentnode = currentnode.next 

    while currentnode!=startnode:
        print(currentnode.data)
        currentnode=currentnode.next 

    currentnode = node4 
    startnode = node4 
    print(currentnode.data)
    currentnode= currentnode.prev

    while currentnode!=startnode:
        print(currentnode.data)
        currentnode=currentnode.prev 

#traversal of a linked list -> same as anything above 
#remove an element 
def removeelement():
    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None 

    def delelement(head, s ): # s= node to delete 
        if head == s:
            return head.next # gives next node 
        
        currentnode = head 
        while currentnode.next and currentnode.next != s : #checking if the next node is not s 
            currentnode=currentnode.next 
        
        if currentnode.next is None:
            return head 
        
        currentnode.next = currentnode.next.next 

        return head

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next=node2
    node2.next = node3
    node3.next = node4 

    delelement(node1,node3)

    currentnode = node1
    while currentnode:
        print(currentnode.data)
        currentnode = currentnode.next 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

def insertelement(head,newnode,position):
    if position==1:
        newnode.next = head 
        return newnode
    
    currentnode = head 
    for _ in range(position-2):
        if currentnode is None:
            break 
        currentnode = currentnode.next 

    newnode.next = currentnode.next 
    currentnode.next = newnode
    return head 


node1.next = node2
node2.next = node3 
node3.next = node4 

newnode = Node(5) 
position = 2 
node1 = insertelement(node1,newnode,position)

currentnode = node1 
while currentnode:
    print(currentnode.data)
    currentnode=currentnode.next 


            

            