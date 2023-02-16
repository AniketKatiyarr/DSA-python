class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class slly:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data,end =" ")
                a = a.next
    def insert(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

n1 = Node(5)
sl = slly()
sl.head=n1
n2 = Node(6)
n1.next = n2
n3 = Node(4)
n2.next = n3
n4 = Node(7)
n3.next = n4
sl.traversal()
sl.insert(90)
sl.traversal()
        
        