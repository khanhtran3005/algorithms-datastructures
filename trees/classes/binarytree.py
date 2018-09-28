
class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    # insert after specific node
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    # insert after specific node
    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # def postorder(self):
    #     print(self.getRootVal())
    #     if self.left:
    #         self.left.postorder()
    #     elif self.right:
    #         self.right.postorder()

import operator
def evaluate(tree):

    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftNode = tree.getLeftChild()
    rightNode = tree.getRightChild()

    if leftNode and rightNode:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftNode), evaluate(rightNode))
    else: #leaf node
        return int(tree.getRootVal())
