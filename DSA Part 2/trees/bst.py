# BST: each node has at most, 2children, the left node is always smaller than the right node, time complex is...
# define Treenode

# define BST
# insert
# delete
# search
# traversls: inorder. postorder, preorder
# bfs and dfs
# is in tree, return outcome from search
# delete tree
# get height of tree
# get successor
# get predecessor
# get min and
# get max


class TreeNode:
    def __init__(self, data=None):
        """
        Initialize a tree node. By default, the data is set to None,
        meaning the node can be used as an empty node initially.
        """
        self.left = None  # Left child
        self.right = None  # Right child
        self.data = data  # Node's data

    def insert(self, data):
        """
        Insert a new node with the specified data into the BST.
        """
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)

    def search(self, data):
        """
        Search for a node with the specified data in the BST.
        Returns True if the data is found, False otherwise.
        """
        if self.data is None:
            return False

        if data == self.data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            return self.left.search(data)
        else:
            if self.right is None:
                return False
            return self.right.search(data)

    def find_min(self):
        """
        Find the node with the minimum value in the subtree rooted at this node.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        """
        Find the node with the maximum value in the subtree rooted at this node.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, data):
        """
        Delete a node with the specified data from the BST.
        """
        if self is None:
            return self

        if data < self.data:
            if self.left is not None:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right is not None:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_larger_node = self.right.find_min()
                self.data = min_larger_node.data
                self.right = self.right.delete(self.data)

        return self

    def pre_order_traversal(self, result=None):
        if result is None:
            result = []
        result.append(self.data)  # Process the current node
        if self.left:
            self.left.pre_order_traversal(result)  # Traverse the left subtree
        if self.right:
            self.right.pre_order_traversal(result)  # Traverse the right subtree
        return result

    def in_order_traversal(self, result=None):
        if result is None:
            result = []
        if self.left:
            self.left.in_order_traversal(result)  # Traverse the left subtree
        result.append(self.data)  # Process the current node
        if self.right:
            self.right.in_order_traversal(result)  # Traverse the right subtree
        return result

    def post_order_traversal(self, result=None):
        if result is None:
            result = []
        if self.left:
            self.left.post_order_traversal(result)  # Traverse the left subtree
        if self.right:
            self.right.post_order_traversal(result)  # Traverse the right subtree
        result.append(self.data)  # Process the current node
        return result

    def bfs(self):
        """
        Perform a breadth-first search (level-order traversal) of the tree.
        """
        result = []
        queue = [self]
        
        while queue:
            current = queue.pop(0)  # Dequeue the first node
            result.append(current.data)  # Process the current node
            
            if current.left:
                queue.append(current.left)  # Enqueue the left child
            if current.right:
                queue.append(current.right)  # Enqueue the right child
                    
        return result
