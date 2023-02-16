#At the beginning

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class traversal:
    def __init__(self):
        self.head = None
    
    def forward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            a = self.head
            while a is not None:
               print(a.data,end =" ")
               a = a.next
    def backward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            print()
            a = self.head
            while a.next is not None:
              a = a.next
            while a is not None:
              print(a.data,end =" ")
              a= a.prev
    def insert_begin(self,data):
        print()
        ns = Node(data)
        a = self.head
        a.prev = ns
        ns.next = n1
        self.head = ns
        
n1 = Node(5)
dll = traversal()
dll.head = n1
n2 = Node(6)
n2.prev = n1
n1.next = n2
n3 = Node(7)
n3.prev = n2
n2.next = n3
n4 = Node(8)
n4.prev = n3
n3.next = n4
dll.forward_traverse()
dll.backward_traverse()
dll.insert_begin(10)
dll.forward_traverse()
dll.backward_traverse()


# At the end

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class traversal:
    def __init__(self):
        self.head = None
    
    def forward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            a = self.head
            while a is not None:
               print(a.data,end =" ")
               a = a.next
    def backward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            print()
            a = self.head
            while a.next is not None:
              a = a.next
            while a is not None:
              print(a.data,end =" ")
              a= a.prev
    def insert_end(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a 

        
n1 = Node(5)
dll = traversal()
dll.head = n1
n2 = Node(6)
n2.prev = n1
n1.next = n2
n3 = Node(7)
n3.prev = n2
n2.next = n3
n4 = Node(8)
n4.prev = n3
n3.next = n4
dll.forward_traverse()
dll.backward_traverse()
dll.insert_end(20)
dll.forward_traverse()
dll.backward_traverse()


# At the required position


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class traversal:
    def __init__(self):
        self.head = None
    
    def forward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            a = self.head
            while a is not None:
               print(a.data,end =" ")
               a = a.next
    def backward_traverse(self):
        if self.head is None:
            print("empty")
        else:
            print()
            a = self.head
            while a.next is not None:
              a = a.next
            while a is not None:
              print(a.data,end =" ")
              a= a.prev
    def insert_pos(self,data,position):
        print()
        np = Node(data)
        a = self.head
        for i in range(1,position-1):
            a = a.next
        np.next = a.next
        np.prev = a
        a.next.prev = np    
        a.next = np
        
n1 = Node(5)
dll = traversal()
dll.head = n1
n2 = Node(6)
n2.prev = n1
n1.next = n2
n3 = Node(7)
n3.prev = n2
n2.next = n3
n4 = Node(8)
n4.prev = n3
n3.next = n4
dll.forward_traverse()
dll.backward_traverse()
dll.insert_pos(30,3)
dll.forward_traverse()
dll.backward_traverse()
