
"""
Height of a tree is the number of nodes along the longest path from the root node to the deepest node
"""
from collections import deque
from treescreation import *


def hightOfTree(root):
    if root is None:
        return True
    else:
        lDepth = hightOfTree(root.left)
        rDepth = hightOfTree(root.right)

        return(1 + max(lDepth, rDepth))
"""
A tree is said to be height balanced, if the balance factor of a node is 0,1 or -1 throughout the tree.
"""
def isTreeBalanced(root):
    if root is None:
        return True
    else:
        lDepth = hightOfTree(root.left)
        rDepth = hightOfTree(root.right)

        """
        root may be balanced, but not the left and right subtrees. So recursively check them.
        """
        if(abs(lDepth - rDepth) <= 1) and isTreeBalanced(root.left) and isTreeBalanced(root.right):
            return True
        else:
            return False

"""
Tree traversals:  Recursive
In Order
Post Order (DFS implementation)
Pre Order (DFS implementation)
"""
"""
    Traverses the binary tree in inorder traversal.

    Args:
        node (Node): The root node of the binary tree.

    Returns:
        None
"""
def inorder_traversal(node):
    _inorder_traversal_recursive(node)

def _inorder_traversal_recursive(node):
    if node is not None:
        _inorder_traversal_recursive(node.left)
        print(node.value)
        _inorder_traversal_recursive(node.right)

"""
    Perform a postorder traversal of a binary tree recursively.

    Args:
        node (Node): The root node of the binary tree.

    Returns:
        None
"""
def postorder_traversal(node):
    _postodrder_traversal_recursive(node)

def _postodrder_traversal_recursive(node):
    if node is not None:
        _postodrder_traversal_recursive(node.left)
        _postodrder_traversal_recursive(node.right)
        print(node.value)
"""
    Performs a preorder traversal of the binary tree starting from the root node.

    Parameters:
        self (BinaryTree): The binary tree instance.
        
        Returns:
            None
"""
def preorder_traversal(node):
    _preorder_traversal_recursive(node)

def _preorder_traversal_recursive(node):
    if node is not None:
        print(node.value)
        _preorder_traversal_recursive(node.left)
        _preorder_traversal_recursive(node.right)


def print_breadth_first(node):
    que = deque([])
    tempNode = None

    if node is not None:
        que.append(node)

    while len(que) > 0:
        tempNode = que.popleft()
        print(tempNode.value)

        if tempNode.left is not None:
            que.append(tempNode.left)

        if tempNode.right is not None:
            que.append(tempNode.right)
    print()