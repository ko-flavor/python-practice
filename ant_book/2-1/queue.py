class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        result = self.queue[0]
        del self.queue[0]
        return result

queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
queue.enqueue("third")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())