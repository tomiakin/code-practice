class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item {item} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop an item")
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self): # top element
        if self.is_empty():
            print("Stack is empty, no items to peek")
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Example usage # This code will only run if the script is executed directly.
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())  # Output: 2
    print(s.pop())  # Output: 1
    print(s.pop())  # Output: Stack is empty, cannot pop an item
