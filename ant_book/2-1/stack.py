class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

stack = Stack()
stack.push("first")
stack.push("second")
stack.push("third")
print(stack.pop())
print(stack.pop())
print(stack.pop())
