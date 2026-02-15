#queue operations are :
#1.enqueue means to add element to the end of the queue
#2.dequeue means to remove an element from the front
#3.peek means to check the first of the element without removing it
#4.size gets the number of elements in the queue
#5.isEmpty it checks if the queue is empty
           #example of a queue using a linked list
class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    # Peek at front element
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get size of queue
    def size(self):
        return len(self.queue)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Queue size:", q.size())
