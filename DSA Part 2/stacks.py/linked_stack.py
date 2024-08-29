class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        print(f"Item {item} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop an item")
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            print("Stack is empty, no items to peek")
            return None
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Example usage
if __name__ == "__main__":
    sll = StackLinkedList()
    sll.push(1)
    sll.push(2)
    print(sll.pop())  # Output: 2
    print(sll.pop())  # Output: 1
    print(sll.pop())  # Output: Stack is empty, cannot pop an item
