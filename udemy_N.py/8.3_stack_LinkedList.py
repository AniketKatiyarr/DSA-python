#Create stack using linked list

class stack:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Sll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        a = self.head
        while a is not None:
            print(a.data,end=" ")
            a = a.next

sl =Sll()

n1 = stack(10)
sl.head = n1

n2 = stack(20)
sl.head = n2
n2.next = n1

n3 = stack(30)
sl.head = n3
n3.next = n2

n4 = stack(40)
sl.head = n4
n4.next = n3

n5 = stack(50)
sl.head = n5
n5.next = n4

sl.traversal()




#PUSH pop peek delete operation of linked list
print()


class stack:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Sll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        a = self.head
        while a is not None:
            print(a.data,end=" ")
            a = a.next
    def push(self,data):
        ne = stack(data)
        a = self.head
        ne.next = a
        self.head = ne

#POP the element
    def pop(self):
        a = self.head
        self.head = a.next
        a.next = None 
#Peek method given the upper element in the stack 
    def peek(self):
        if self.head is None:
            print("Empty stack")
        else:
            print(self.head.data) 

#Isempty method of stack
    def isempty(self):
        if self.head is None:
            print(True)
        else:
            print(False)  
#Delete the stack
    def delete(self):
        a = self.head
        self.head = None
        a.next = None

        
sl =Sll()

n1 = stack(10)
sl.head = n1

n2 = stack(20)
sl.head = n2
n2.next = n1

n3 = stack(30)
sl.head = n3
n3.next = n2

n4 = stack(40)
sl.head = n4
n4.next = n3

n5 = stack(50)
sl.head = n5
n5.next = n4

print("Push() the element in stack:-")
sl.push(60)
sl.traversal()

print("\nPop() the element in stack:-")
sl.pop()
sl.traversal()

print("\nThe element at the top of the stack is:-")
sl.peek()

print("Is stack is empty:-")
sl.isempty()

print("Delete entire stack:-")
sl.delete()


