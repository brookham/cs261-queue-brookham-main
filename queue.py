# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.

# Name: Brook Hamilton
# Collaborators:
# Time spent:

#Note: If you're having trouble installing llist, use pyllist instead
#from pyllist import sllist

from llist import sllist

class Queue:
    def __init__(self, items = 0):
        self.items = items
        self.data = sllist()

    def enqueue(self, item):
        self.data.append(item)
        self.items += 1

    def dequeue(self):
        if self.items == 0:
            raise ValueError("Queue already empty")
        self.items -= 1
        return self.data.popleft()
    
    def is_empty(self):
        if self.items == 0:
            return True
        else:
            return False
        
    def size(self):
        return self.items # type: ignore