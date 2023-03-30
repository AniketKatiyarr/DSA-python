#Deletion at the beginning of the doubly linked list
print("Delete at the beginning:-")

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
         self.head = None
        #  self.next = None
        #  self.prev = None
    
    def traversal(self):
        if self.head is None:
            return "Empty linked list"
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
    def DeleteAtTheBeginning(self):
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None
        
        
dl = Dll()
n1 = node(1)
dl.head = n1

n2 = node(2)
n1.next =n2
n2.prev = n1

n3 = node(3)
n2.next =n3
n3.prev = n2

n4 = node(4)
n3.next =n4
n4.prev = n3

n5 = node(5)
n4.next =n5
dl.DeleteAtTheBeginning()
dl.traversal()
print()



#Deletion at the end of the doubly linked list
print()
print("Delete at the end")

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
         self.head = None
        #  self.next = None
        #  self.prev = None
    
    def traversal(self):
        if self.head is None:
            return "Empty linked list"
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
    def DeleteAtTheEnd(self):
        b = self.head.next
        a = self.head
        while b.next is not None:
            a = a.next
            b = b.next 
        a.next = None
        b.prev = None       
        
        
dl = Dll()
n1 = node(1)
dl.head = n1

n2 = node(2)
n1.next =n2
n2.prev = n1

n3 = node(3)
n2.next =n3
n3.prev = n2

n4 = node(4)
n3.next =n4
n4.prev = n3

n5 = node(5)
n4.next =n5
dl.DeleteAtTheEnd()
dl.traversal()
print()



#Deletion at the  required postion

print("Delete at the position:-")


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
         self.head = None
        #  self.next = None
        #  self.prev = None
    
    def traversal(self):
        if self.head is None:
            return "Empty linked list"
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
                
    def DeleteAtThePosition(self,pos):
        a = self.head.next
        b = self.head
        if b is None:
            return "Linked list is empty"
        else:
            for i in range(1,pos-1):
                a = a.next
                b = b.next
            b.next = a.next
            a.next.prev = b
    def DeleteEntireDLL(self):
        a = self.head
        self.head = None
        a.next = None
        
            
dl = Dll()
n1 = node(1)
dl.head = n1

n2 = node(2)
n1.next =n2
n2.prev = n1

n3 = node(3)
n2.next =n3
n3.prev = n2

n4 = node(4)
n3.next =n4
n4.prev = n3

n5 = node(5)
n4.next =n5
dl.DeleteAtThePosition(3)
dl.traversal()
dl.DeleteEntireDLL()
dl.traversal()