from queue import LifoQueue

stack = LifoQueue()

stack.put(100)
stack.put(200)

print(stack.get())   # 200
