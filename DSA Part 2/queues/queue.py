class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item {item} enqueued")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue an item")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            print("Queue is empty, no items to peek")
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)


# Example usage
if __name__ == "__main__":  # This code runs only when the script is executed directly.
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print(q.dequeue())  # Output: Queue is empty, cannot dequeue an item
