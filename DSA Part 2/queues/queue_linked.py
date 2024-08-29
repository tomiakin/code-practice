class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Item {item} enqueued")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue an item")
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            print("Queue is empty, no items to peek")
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print(q.dequeue())  # Output: Queue is empty, cannot dequeue an item
