#Delete at the beginning of the doubly linked list
print("Delete at the beginning:-")
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
   
    def DeleteAtTheBeginning(self):
        a = self.head
        self.tail.next = a.next
        self.head.prev = a.next
        self.head = a.next
        self.head.prev = None
        
        
        
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

cdl.DeleteAtTheBeginning()
cdl.traversal()





#Deletion at the end of the circular doubly linked list
print()
print("delete at the end:-")




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
    def DeleteAtTheEnd(self):
        self.tail = self.tail.prev
        self.tail.next  = self.head
        self.head.prev = self.tail

        
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

cdl.DeleteAtTheEnd()
cdl.traversal()







#Delete at the required position of doubly linked list
print()
print("Delete at the required position:-")


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
    
    def DeleteAtThePosition(self,pos):
        b = self.head
        a = self.head.next
        if pos == 1:
            self.tail.next = b.next
            self.head = b.next
            self.head.prev = self.tail
        else:
            for i in range(1,pos-1):
                a = a.next
                b = b.next
            b.next = a.next
            a.next.prev = a.prev

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

cdl.DeleteAtThePosition(1)
cdl.traversal()
cdl.DeleteAtThePosition(4)
print()
cdl.traversal()
        
        
        

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
    
    def EntireCDLL(self):
        a = self.head
        a.next = None
        self.head.prev = None
        self.head = None
        self.tail.next = None
        return "Linked list is Empty"
    
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
    
print()
print(cdl.EntireCDLL())


