
from queue import LifoQueue
stack = LifoQueue(maxsize = 2)
stack.put("Lemon")
stack.put("mango")
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
print(stack)