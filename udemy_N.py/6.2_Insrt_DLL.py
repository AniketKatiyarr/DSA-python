#Insert at the beginning of the doubly linked list
print("Insertion at the beginning:-")
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
    
    def InsertAtTheBeginning(self,data):
        a = self.head
        ne = node(data)
        if a is None:
            self.head = ne
            self.tail = ne
        else:
            ne.next = self.head #a also
            a.prev = ne
            self.head = ne
            ne.prev = None        
                            
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
n5.prev = n4

dl.InsertAtTheBeginning(0)
dl.traversal()






#Insert at the End of the doubly linked list
print()
print("Insertion at the end:-")

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
                
    def InsertAtTheEnd(self,data):
        a = self.head
        ne = node(data)
        while a.next is not None:
            a = a.next
        a.next =  ne
        ne.prev = self.head
        ne.next = None
        
   
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
n5.prev = n4

dl.InsertAtTheEnd(6)
dl.traversal()     
        
        
#Insert at the required position in doubly linked list
print()
print("Insert at the position:-")


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
    def InsertAtThePosition(self,pos,data):
        a = self.head
        ne = node(data)
        for i in range(1,pos-1):
            a = a.next
        ne.next = a.next
        ne.prev = self.head
        a.next = ne
        a.next.prev = ne


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
n5.prev = n4

dl.InsertAtThePosition(6,66)
dl.traversal()                    
               