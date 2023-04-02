class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
 #mera method    
    def traversal(self):
        a = self.tail
        print(a.data,end=" ")
        a = a.prev
        while a != self.head:
            print(a.data,end=" ")
            a =a.prev
        print(a.data,end=" ")
#Second method by udemy

        # a = self.tail
        # while a:
        #     print(a.data,end=" ")
        #     if a == self.head:
        #         break
        #     a = a.prev
                    
cdl = CDLL()
n1 = node(10)
cdl.head = n1
cdl.tail = n1

n2 = node(20)
n1.next = n2 
n2.prev = n1 
cdl.tail = n2
cdl.tail.next = cdl.head


n3 = node(30)
n2.next = n3 
n3.prev = n2 
cdl.tail = n3
cdl.tail.next = cdl.head


n4 = node(40)
n3.next = n4
n4.prev = n3 
cdl.tail = n4
cdl.tail.next = cdl.head


n5 = node(50)
n4.next = n5 
n5.prev = n4
cdl.tail = n5
cdl.tail.next = cdl.head

cdl.traversal()