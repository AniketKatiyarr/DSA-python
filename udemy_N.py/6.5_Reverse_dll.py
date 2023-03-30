class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
         self.head = None
         self.tail = None
        #  self.next = None
        #  self.prev = None
    
    def traversal(self):
        if self.head is None:
            return "Empty linked list"
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
    def reverse(self):
        a = self.tail
        while a:
            print(a.data,end=" ")
            a = a.prev
            

dl = Dll()
n1 = node(1)
dl.head = n1
dl.tail = n1



n2 = node(2)
n1.next =n2
n2.prev = n1
dl.tail = n2
dl.tail.next = n2



n3 = node(3)
n2.next =n3
dl.tail = n3
n3.prev = n2
dl.tail.next = n3


n4 = node(4)
n3.next =n4
dl.tail = n4
n4.prev = n3

dl.tail.next = n4



n5 = node(5)
dl.tail = n5
n4.next =n5

print(dl.reverse())
dl.traversal()
