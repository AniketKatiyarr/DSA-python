class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class cll:
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
        
    def search(self,value):
        a = self.head
        count = 1
        if a is None:
            return "No!! value in linked list"
        else:
            while a.next != self.head:
                if a.data == value:
                    return True ,  count
                else:
                    count += 1
                a = a.next
            if a.data == value:
                return True,count
            else:
                return "Value not in linked list"

      
                
    
cl = cll()
n1 = node(1)
cl.head = n1
cl.tail = n1
cl.tail.next = cl.head

n2 = node(2)
cl.tail.next = n2
cl.tail = n2
cl.tail.next = cl.head

n3 = node(3)
cl.tail.next = n3
cl.tail = n3
cl.tail.next = cl.head


n4 = node(4)
cl.tail.next = n4
cl.tail = n4
cl.tail.next = cl.head


n5 = node(5)
cl.tail.next = n5
cl.tail = n5
cl.tail.next = cl.head
print(cl.search(3))
print(cl.search(5))
print(cl.search(6))
cl.traversal()


