#at the beginning
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

    def delete_begining(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
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
sl.delete_begining()
sl.traversal()
 
 
#deletion from the end

dte = self.head
a = self.head.next
while a.next is not None:
    a = a.next
    dte = dte.next
dte.next = None    

#deletion at the specific position

prev = self.head
a = self.head.next
for i in range(1,position -1):
    a = a.next
    prev = prev.next
prev.next = None
a.next = None
