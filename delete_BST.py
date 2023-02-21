class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    
def inorder(root):
    if root is not None:
        inorder(root.left)
    
        print(str(root.key)+"->",end=' ')
        inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right, key)
        
    return node

def delete(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = delete(node.left,key)
    else:
        node.right = delete(node.right, key)
        
    return node

#def search(root,key):
#    if key == root.key:
#        return root.key
#    if key > root.key:
#        if root.right is None:
#            print("Not found")
#        return root.right.search(key)
#    elif key < root.key:
#        if root.left is None:
#            print("not found")
#        return root.left.search(key)
#    else:
#        return root.key
def search(root,key):
    if root.key is None or root.key==key:
        return root
    if root.key > key:
        return search(root.left,key)
    if root.key<key:
        return search(root.right,key)
    

root = Node(1)
root = insert(root,23)
root = insert(root,20)
root = insert(root,5)
root = insert(root,8)
root = insert(root,4)
root = insert(root,3) 
inorder(root)

        
print(search(root,20))
print(search(root,21))
print(search(root,4))

