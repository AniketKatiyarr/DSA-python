#Deletion at the beginning

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
    def DeleteAtTheBeginning(self):
    #    if self.next == self.trail:
    #        self.next = None
    #        self.trail = None
    #    else:
           a = self.head
           self.head = a.next
           a.next = None
           
                  
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
# sly.traversal()
sly.DeleteAtTheBeginning()
print()
sly.traversal()



#Deletion at the End of the singly linked list

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
    def DeleteAtTheEnd(self):                
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next 
        prev.next = None
        prev = self.head


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
# sly.traversal()
sly.DeleteAtTheEnd()
print()
sly.traversal()        




            
#delete the at the required position

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
    def DeleteAtThePosition(self,position):
        a = self.head
        for i in range(1,position-1):
            a = a.next
        nextnode = a.next
        a.next = nextnode.next         
        
        
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
# sly.traversal()
sly.DeleteAtThePosition(4)
print()
sly.traversal()




    
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
    def enitreSLL(self):
     self.head = None
     
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
# sly.traversal()
sly.enitreSLL()
print()
sly.traversal()