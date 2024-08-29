class Node:

    """
    An object for storing a single node of a linked list.
    Models two atrributes - data and the link to the next node in the list
    """

    # data is the element of the list
    # next node is the next element
    data = None
    next_node = None

    # initialise any object 
    def __init__(self, data):
        self.data = data

    # string func to present when called
    def __repr__(self):
        return f"<Node data: {self.data}>"
    
class LinkedList:

    """
    Singly linked list
    """

    def __init__(self):
        self.head = None # this also creates a head variable to be used in the class

    # Returns a boolean to check if list is empty
    def is_empty(self):
        return self.head == None
    

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time 
        """
        current = self.head # current element
        count = 0 # counter for number of elemnts

        # Traverse the list and count the nodes
        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list
        takes constant time which is the best case
        because its just a reassignment!
        """
        new_node = Node(data) # create a new node
        new_node.next_node = self.head # make the next node after new node the 'old' head
        self.head = new_node # set our newly established node as head

    def search(self, key):
        current = self.head

        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index): # note self is always the list here

        """
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point
        takes O(n) time, so overall this is O(n)
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data) # create a new node to store the data to insert
            
            position = index
            current = self.head

            while position > 1: # when loop ends, current will hold the node just before the insert point
                current = current.next_node # as long as we are not at 'posiiton-1' keep moving to the next node
                position -= 1

            # the prev and next nodes to our 'new_node'
            # prev_node -> new_node -> next_node
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node # note difference between attribute and variable

    def remove(self, key): # remove with a key i.e some data, if it was index instead we need a search?

        """
        Removes Node conntaininf data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None #keep track of prev node as we traverse list
        found = False # a stopping cond 

        #1st cobd checks we are not after tail (will be not next node), 2nd keep going, stops when Found=True as not found is False
        # this is a boolean i.e True and True needed
        while current and not found: 
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current # just returns the node that was removed not necessary
            

    def __repr__(self) -> str:
        """
        Return a string representation of the list
        note "data" woll always work as it is the input to creaet any node
        N1 = Node(data)
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None: # we are at the last element i.e tail
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
        
            current = current.next_node 

        return "-> ".join(nodes)
        


"""
- to add the functions: remove at index
- what is the node at index x?
cd DSA_2
Run python3 -i linked_list.py in terminal

>>> N1 = Node(10)
>>> N1
<Node data: 10>
>>> N2 = Node(20)
>>> N1.next_node = N2
>>> N1.next_node
<Node data: 20>
>>> N2
<Node data: 20>

"""