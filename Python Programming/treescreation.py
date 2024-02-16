class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    """
        Inserts a new node with the given value into the binary search tree.

        Parameters:
            value (any): The value to be inserted into the binary search tree.

        Returns:
            None
    """
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
            
    """
        Inserts a new node with the given value into the binary search tree recursively.

        Parameters:
            node (Node): The root node of the binary search tree.
            value (int): The value to be inserted into the tree.

        Returns:
            None
    """
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
