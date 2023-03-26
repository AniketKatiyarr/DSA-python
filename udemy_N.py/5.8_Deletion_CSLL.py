#Delete the node at the beginning of the linked list
print("Delete at beginning:-")
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
    def DeleteATTheBeginning(self):
        a = self.head
        self.head = a.next
        self.tail.next = a.next
        self.tail.next = a.next
        # self.tail.next = a
        # a = None

        

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

n5 = node(50)
cl.tail.next = n5
cl.tail = n5
cl.tail.next = cl.head

cl.DeleteATTheBeginning()
cl.traversal()



#Deletion at the end of the linked list
print()
print("Deletion at the end:-")


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
    def DeleteATTheEnd(self):
        a = self.head
        while a.next != self.tail:
            a = a.next
        a.next = self.head
        self.tail = None
        self.tail = a         
        
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

n5 = node(50)
cl.tail.next = n5
cl.tail = n5
cl.tail.next = cl.head

cl.DeleteATTheEnd()
cl.traversal()


#Delete at the required position
print()
print("Delete at the required position:-")



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
    def DeleteAtTheRequiredPosition(self,pos):
        if pos == 1:
            a = self.head
            self.head = None
            self.head = a.next
            self.tail.next = self.head
        else:    
            a = self.head
            for i in range(1,pos-1):
                a = a.next
            nextnode = a.next
            a.next = nextnode.next           
            
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

n5 = node(50)
cl.tail.next = n5
cl.tail = n5
cl.tail.next = cl.head

cl.DeleteAtTheRequiredPosition(1)
cl.DeleteAtTheRequiredPosition(3)
cl.traversal()
print()


#Deletion entire singly circular linked list


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
    def delete_entire_CSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        print("Whole circular singly linked list is deleted:-")
        print("Deleted already...!!")

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

n5 = node(50)
cl.tail.next = n5
cl.tail = n5
cl.tail.next = cl.head

cl.delete_entire_CSLL()
cl.traversal()
