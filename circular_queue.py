class queue:
    def __init__(self,limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear =  None
        self.size = 0
    
    def isEmpty(self):
        return self.size<=0
    
    def enqueue(self,item):
        if self.size >= self.limit:
            print("queue overflow")
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("queue after enqueue:",self.que) 
    
    def dequeue(self):
        if self.size <=0:
            print("queue underflow") 
        else:
            self.que.pop(0)
            self.size -= 1 
            if self.size ==0:
                self.front = self.rear = None
            else:
                self.rear = self.size -1
            print("queue after dequeue:",self.que)
    def queueRear(self):
        if self.rear is None:
            print("sorry queuee is empty")
            raise IndexError
        return self.que[self.rear]
    def queueFront(self):
        if self.front is None:
            print("sorry,empty hsi")
            raise IndexError
        return self.que[self.front]
    def size(self):
        return self.size                            

q = queue()
q.enqueue("first")
print("front",q.queueFront())
print("rear",q.queueRear())
q.enqueue("second")
print("front",q.queueFront())
print("rear",q.queueRear())
q.enqueue("third")
print("front",q.queueFront())
print("rear",q.queueRear())
q.enqueue("fourth")
q.dequeue()   
