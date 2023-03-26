#Insert the node at the beginning of the circular linked list 
print('Insert the node at the begiining of the circular linked list:-')
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class cll:
    def __init__(self):
        self.head = None
        self.tail = None
                
    def traversal(self):
        if self.head is None:
            return "there is nothing to traverse"
        else:
            a = self.head
            print(a.data,end=" ")
            a = a.next
            while a.next != self.head:
                print(a.data,end=" ")
                a = a.next
            print(a.data,end=" ")
    def insertAtTheBeginning(self,data):
        ne = node(data)
        if self.head is None:
            self.head = ne
            self.tail = ne
            self.tail.next = ne
        else:
             ne.next = self.head
             self.head = ne
             self.tail.next = ne
        

cl = cll()
n1 = node(10)
cl.head = n1
cl.tail = n1
cl.tail.next = cl.head

n2 = node(20)
cl.tail.next = n2
cl.tail = n2
cl.tail.next = cl.head

n3 = node(30)
cl.tail.next = n3
cl.tail = n3
cl.tail.next = cl.head

n4 = node(40)
cl.tail.next = n4
cl.tail = n4
cl.tail.next = cl.head
cl.insertAtTheBeginning(5)
cl.traversal()



#Insert the node at the end of the circular linked list

#First method create and traverse of cicular singly linked list
print()
print("Insert the node at the end of the circluar linked list:-")

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class cll:
    def __init__(self):
        self.head = None
        self.tail = None
                
    def traversal(self):
        if self.head is None:
            return "there is nothing to traverse"
        else:
            a = self.head
            print(a.data,end=" ")
            a = a.next
            while a.next != self.head:
                print(a.data,end=" ")
                a = a.next
            print(a.data,end=" ")
    def insertAtTheEnd(self,data):
        ne = node(data)
        ne.next = self.tail.next
        self.tail.next = ne
        self.tail = ne
        

cl = cll()
n1 = node(10)
cl.head = n1
cl.tail = n1
cl.tail.next = cl.head

n2 = node(20)
cl.tail.next = n2
cl.tail = n2
cl.tail.next = cl.head

n3 = node(30)
cl.tail.next = n3
cl.tail = n3
cl.tail.next = cl.head

n4 = node(40)
cl.tail.next = n4
cl.tail = n4
cl.tail.next = cl.head
cl.insertAtTheEnd(50)
cl.traversal()


#Insert at the required position:

print()
print("insert at the required position:-")


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class cll:
    def __init__(self):
        self.head = None
        self.tail = None
                
    def traversal(self):
        if self.head is None:
            return "there is nothing to traverse"
        else:
            a = self.head
            print(a.data,end=" ")
            a = a.next
            while a.next != self.head:
                print(a.data,end=" ")
                a = a.next
            print(a.data,end=" ")
    def InsertAtThePosition(self,pos,data):
        ne = node(data)
        if pos == 1:
            ne.next = self.head
            self.head = ne
            self.tail.next = ne            
        else:
            a = self.head
            for i in range(1,pos-1):
                a = a.next
            ne.next = a.next
            a.next = ne
            
cl = cll()
n1 = node(10)
cl.head = n1
cl.tail = n1
cl.tail.next = cl.head

n2 = node(20)
cl.tail.next = n2
cl.tail = n2
cl.tail.next = cl.head

n3 = node(30)
cl.tail.next = n3
cl.tail = n3
cl.tail.next = cl.head

n4 = node(40)
cl.tail.next = n4
cl.tail = n4
cl.tail.next = cl.head
cl.InsertAtThePosition(3,90)
cl.traversal()








