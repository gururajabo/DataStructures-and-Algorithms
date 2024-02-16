'''
Dictionaries can be constructed using BST, AVL trees, hash tables, splay trees, and B-trees
Dictionaties(key value pair) is a data structures while facilitates faster retrivel of data.

BST: Supports faster searching, rapid sorting, easy insertion and deletion. 
'''
from treescreation import *
from treeoperationsimplementation import * 

def bst_search(root, key):
    if root is None:
        return False
    if root.value == key:
        return True
    if root.value > key:
        return bst_search(root.left, key)
    else:
        return bst_search(root.right, key)


def bst_insert(root, key):
    if root is None:
        return Node(key)
    if root.value > key:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)    
    return root

def bst_delete(root, key):
    if root is None:
        return None
    if root.value > key:
        root.left = bst_delete(root.left, key)
    elif root.value < key:
        root.right = bst_delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.value = temp.value
        root.right = bst_delete(root.right, temp.value)
    return root
    
# Example usage:
tree = BinaryTree()
print("BST Insert")
tree.root = bst_insert(tree.root, 50)
tree.root = bst_insert(tree.root, 30)
tree.root = bst_insert(tree.root, 20)
tree.root = bst_insert(tree.root, 10)
tree.root = bst_insert(tree.root, 70)
tree.root = bst_insert(tree.root, 100)

print("BST In order traversal")
inorder_traversal(tree.root)

print("BST Search")
print("Searching a value {} in BST {}".format(1000, bst_search(tree.root, 1000)))


print("BST Delete")
tree.root = bst_delete(tree.root, 70)
inorder_traversal(tree.root)