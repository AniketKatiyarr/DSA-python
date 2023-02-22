class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def search(self,val):
        if self.data > val:
            if self.left is None:
                return "node not present:",self.data
            return self.left.search(val)
        elif self.data <val:
            if self.right is None:
                return "node is not present:",self.data
            return self.right.search(val)
        else:
            return "key i found in tree" ,self.data
         
                    
     
def inorder(root):
    if root is not None:
        inorder(root.left)
    
        print(str(root.data)+"->",end=' ')
        
        inorder(root.right)

def insert(node,data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right, data)
        
    return node

#def search(root,key):
#    if root.data is None:
#        return None
#    if root.data == key:
#        return root.data
#    if root.data > key:
#        root.left = search(root.left,key)
#    else:
#       root.right =  search(root.left,key)


            
            
            
            
    
   
root = Node(7)
root = insert(root,23)
root = insert(root,20)
root = insert(root,5)
root = insert(root,8)
root = insert(root,4)
root = insert(root,3) 
inorder(root)      
print()  


print(root.search(5))
print(root.search(9))                


