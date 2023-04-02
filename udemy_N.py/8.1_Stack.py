#Stack as a list method

'''
operations:-
             push(),pop(),isempty(),isfull(),size(),delete(),peek()
             
             peek()  = give top element but not delete it
             isfull() = isfull give size limit of stack 
             
             '''
stack=[]

stack.append("Aniket")
stack.append("Rishabh")
print(stack)

stack.pop()
print(stack)





#Second method

class stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(i)for i in self.list]
        return ' '.join(values)    
    
    #isEMpty
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
    
    #push
    def push(self,data):
        self.list.append(data)
        return "Item added successfully..!!"
    
    #pop
    def pop(self):
        if self.isempty():
             print("NO element to pop()")
        else:
            self.list.pop()
            return "Element pop succesfullly..!!"
    
    #peek
    def peek(self):
        if self.isempty():
            print("NO element to Display")
        else:
            return self.list[len(self.list)-1]
    
    #Delete stack
    def delete(self):
        self.list = None

s = stack()
print(s.isempty())

s.push("1")
s.push("2")
s.push("3")
print(s)

s.pop()
print(s)

print(s.peek())



 