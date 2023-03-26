#Basic Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.trail = None

class sll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        a = self.head
        if a is None:
            print("Linked list is empty")
        else:   
             while a is not None:
                 print(a.data,end=" ")
                 a = a.next
            
n1 = Node(1)
sly = sll()
sly.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
sly.traversal()




