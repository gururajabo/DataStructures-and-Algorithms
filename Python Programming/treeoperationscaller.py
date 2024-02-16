from treescreation import *
from treeoperationsimplementation import *

# Example usage:
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(90)
tree.insert(100)
tree.insert(110)

print("inorder traversal")
inorder_traversal(tree.root)
print("preorder traversal")
preorder_traversal(tree.root)
print("postorder traversal")
postorder_traversal(tree.root)

heightOfTree = hightOfTree(tree.root)
print("Height of a Binary tree is {}".format(heightOfTree))

isBalanced = isTreeBalanced(tree.root)
print("Is Binary tree balanced? {}".format(isBalanced))

'''
BFS implementation
'''
print_breadth_first(tree.root)







