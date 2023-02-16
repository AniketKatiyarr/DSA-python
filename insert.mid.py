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
    
    def insert(self,position,data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1,position):
            a = a.next
        nib.next = a.next
        a.next = nib
 
n1 = Node(16)
sl = slly()
sl.head=n1
n2 = Node(13)
n1.next = n2
n3 = Node(7)
n2.next = n3
n4 = Node(0)
n3.next = n4
sl.traversal()
sl.insert(2,1)
sl.traversal()       