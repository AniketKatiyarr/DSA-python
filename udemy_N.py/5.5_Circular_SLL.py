#First method create and traverse of cicular singly linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class cll:
    def __init__(self):
        self.head = None
        self.tail = None
#first method given by hary bhaia

    # def traversal(self):
    #     if self.head is None:
    #         return "Empty circular linked list"
    #     else:
    #         temp = self.head
    #         print(temp.data,end=" ")
    #         while temp.next != self.head:
    #             temp = temp.next 
    #             print(temp.data,end=" ")

#second method given by me                
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

cl.traversal()


