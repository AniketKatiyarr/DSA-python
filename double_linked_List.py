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


           