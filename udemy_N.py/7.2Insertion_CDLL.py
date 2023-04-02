#Inseert at the beginning of the circular doubly linked list
print("Insert at the beginning:-")
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traversal(self):
        a = self.head
        print(a.data,end=" ")
        a = a.next
        while a.next != self.head:
            print(a.data,end=" ")
            a = a.next 
        print(a.data,end=" ")
    def InsertAtTheBeginning(self,data):
        ne = node(data)
        a =self.head
        ne.next = self.head
        a.prev = ne
        self.head = ne
        self.tail.next = ne 
        ne.prev = self.tail                          
        
cdl = CDLL()
n1 = node(10)
cdl.head = n1
cdl.tail = n1

n2 = node(20)
n1.next = n2 
n2.prev = n1 
cdl.tail = n2
cdl.tail.next = cdl.head


n3 = node(30)
n2.next = n3 
n3.prev = n2 
cdl.tail = n3
cdl.tail.next = cdl.head


n4 = node(40)
n3.next = n4
n4.prev = n3 
cdl.tail = n4
cdl.tail.next = cdl.head


n5 = node(50)
n4.next = n5 
n5.prev = n4
cdl.tail = n5
cdl.tail.next = cdl.head

cdl.InsertAtTheBeginning(5)
cdl.traversal() 




#Insert at the end of the doubl linked list
print()
print("Insert at the end:-")



#Inseert at the  End of the dounly circular linked list
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traversal(self):
        a = self.head
        print(a.data,end=" ")
        a = a.next
        while a.next != self.head:
            print(a.data,end=" ")
            a = a.next 
        print(a.data,end=" ")   
    def InsertAtTheEnd(self,data):
        ne = node(data)
        a = self.head
        ne.next = self.head
        ne.prev = self.tail
        self.tail.next = ne
        self.head.prev = ne 
        self.tail = ne                  
cdl = CDLL()
n1 = node(10)
cdl.head = n1
cdl.tail = n1

n2 = node(20)
n1.next = n2 
n2.prev = n1 
cdl.tail = n2
cdl.tail.next = cdl.head


n3 = node(30)
n2.next = n3 
n3.prev = n2 
cdl.tail = n3
cdl.tail.next = cdl.head


n4 = node(40)
n3.next = n4
n4.prev = n3 
cdl.tail = n4
cdl.tail.next = cdl.head


n5 = node(50)
n4.next = n5 
n5.prev = n4
cdl.tail = n5
cdl.tail.next = cdl.head

cdl.InsertAtTheEnd(60)
cdl.traversal()                   
        
        
        

#Inseert at the  End of the dounly circular linked list
print()
print("Insert at the required position:-")


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traversal(self):
        a = self.head
        print(a.data,end=" ")
        a = a.next
        while a.next != self.head:
            print(a.data,end=" ")
            a = a.next 
        print(a.data,end=" ")
    
    def InsertAtTheRequired(self,pos,data):
             a = self.head.next 
             b = self.head  
             ne = node(data)
             for i in range(1,pos-1):
                 a = a.next
                 b = b.next
             ne.next = b.next
             b.next = ne
             ne.prev = a.prev
             a.prev = ne
             

cdl = CDLL()
n1 = node(10)
cdl.head = n1
cdl.tail = n1

n2 = node(20)
n1.next = n2 
n2.prev = n1 
cdl.tail = n2
cdl.tail.next = cdl.head


n3 = node(30)
n2.next = n3 
n3.prev = n2 
cdl.tail = n3
cdl.tail.next = cdl.head


n4 = node(40)
n3.next = n4
n4.prev = n3 
cdl.tail = n4
cdl.tail.next = cdl.head


n5 = node(50)
n4.next = n5 
n5.prev = n4
cdl.tail = n5
cdl.tail.next = cdl.head

cdl.InsertAtTheRequired(3,999)
cdl.InsertAtTheRequired(0,999)
cdl.traversal()      