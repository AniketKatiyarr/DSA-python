class stack:
    def __init__(self,maxsize):
        self.list = []
        self.maxsize = maxsize
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(i)for i in self.list]
        return " ".join(values)
    
    #isEmpty
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
   
   #Isfull method
    def isfull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
               
    #push method
    def push(self,value):
        if self.isfull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "element added successfully..!"    
    #delete
    def delete(self):
        self.list = None
        
    #peek
    def peek(self):
        if self.list == []:
            return "No element to show"
        else:
            return self.list[(len(self.list)-1)]

s = stack(4)
print(s.isempty())
print(s.isfull())

s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.peek())

print(s)


