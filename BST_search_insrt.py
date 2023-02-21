class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
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

def MinValue(node):
    print()
    current = node
    while current is not None:
        current = current.left
    return current

root = Node(7)
root = insert(root,23)
root = insert(root,20)
root = insert(root,5)
root = insert(root,8)
root = insert(root,4)
root = insert(root,3) 
inorder(root)

MinValue(root)




