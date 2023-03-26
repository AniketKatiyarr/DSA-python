print("Insert At the beginning of the linked list:-")
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
    def InserAtTheBeginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
                   
                   
                   
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

sly.InserAtTheBeginning(0)
sly.traversal()


print()
print("Insert At the End of the singly linkd list:-")
#Insert At The End of the linked list

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
    def InsertAtTheEnd(self,data):
        a = self.head
        ne = Node(data)
        while a.next is not None:
            a = a.next
        a.next = ne


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

sly.InsertAtTheEnd(6)
sly.traversal()


print()
print("Insert at the Required position:-")

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
    def InsertAtThePosition(self,position,data):
        nb = Node(data)
        a = self.head
        for i in range(1,position):
            a = a.next
        
        nb.next = a.next
        a.next = nb
        
        
                 
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
sly.InsertAtThePosition(3,100)
sly.traversal()