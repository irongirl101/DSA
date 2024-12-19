#Singly Linked List 

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