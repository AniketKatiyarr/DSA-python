class Node:
    def __init__(self,data):
      self.data  = data
      self.next = None

class sll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            pass
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next


n1 = Node(8)
sl = sll()
sl.head=n1
n2 = Node(3)
n1.next = n2
n3 = Node(1)
n2.next = n3
n4 = Node(99)
n3.next = n4
sl.traversal()