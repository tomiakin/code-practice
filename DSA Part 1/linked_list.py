class Node:

    """
    An object for storing a single node of a linked list.
    Models two atrributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"
    
class LinkedList:

    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time 
        """
        current = self.head
        count = 0

        # Traverse the list and count the nodes
        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list
        takes constant time which is the best case
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node