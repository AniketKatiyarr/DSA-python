class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self,data):
        if self is None:
            return Node(data)
        if data < self.data:
            self.left = self.left.insert(data)
        else:
            self.right = self.right.insert(data)
            
        return 
    
def inorder(root):
    if root is not None:
        inorder(root.left)
    
        print(str(root.data)+"->",end=' ')
        
        inorder(root.right)

    

#def search(root,key):
#        if root.data ==key:
#           print("not is found")
#           return 
#        if root.data < key:
#            if root.left:
#                root.left.search(key)
#                return
#            else:
#                print("node is not found")
#        else:
#            if root.data > key:
#                if root.right:
#                    root.right.search(key)
#                    return
#                else:
#                    print("node not found")
                       
    
    
    
    
    
    
root = Node(1)
root = Node(23)
root = Node(20)
root = Node(5)
root = Node(8)
root = Node(4)
root = Node(3) 
inorder(root)

#search(root,3)