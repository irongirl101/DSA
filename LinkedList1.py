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




            

            