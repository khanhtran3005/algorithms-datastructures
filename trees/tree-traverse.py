from classes.binarytree import BinaryTree


def postorder(tree):
    # print root node last
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    # print nodes in ascending order
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def preorder(tree):
    # print root node first
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


tree = BinaryTree(2)
tree.insertLeft(1)
tree.insertRight(3)
tree.getLeftChild().insertLeft(0)
tree.getLeftChild().insertLeft(7)
tree.getRightChild().insertLeft(9)
tree.getRightChild().insertRight(1)

"""
        2
      /   \
     1     3
    / \   / \
   0   7 9   1

"""
preorder(tree)
print("-------")
inorder(tree)
print("-------")
postorder(tree)
