class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key
    
    def TraPreOrder(self):
       print(self.val,end=" ")
       if self.left:
           self.left.TraPreOrder()
       if self.right:
           self.right.TraPreOrder()
    
    def TraInOrder(self):
        if self.left:
            self.left.TraInOrder()
        print(self.val,end= " ")
        if self.right:
            self.right.TraInOrder()
    
    def TraPostOrder(self):
        if self.left:
            self.left.TraPostOrder()
        if self.right:
            self.right.TraPostOrder()
        print(self.val,end=" ")

root =Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("pre order:",end = " ") 
root.TraPreOrder()
print("\npost order:",end =" ")
root.TraPostOrder()
print("\nInorder:",end=" ") 
root.TraInOrder()

print()

