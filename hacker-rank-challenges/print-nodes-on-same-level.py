from math import log, ceil


class BinaryTree:

    def __init__(self, value: int = None):
        """Binary tree's constructor

        Keyword Arguments:
            value {in} -- node's value (default: {None})
        """
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, newNode: int = None):
        """Insert new node to the left

        Arguments:
            newNode {int} -- value of new node (default: {None})
        """
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            """if right child is not empty, new node will be inserted
            to the right of current node and right child
            """
            t = BinaryTree(newNode)
            t.left = self.left  # new node holds parent's left child
            self.left = t  # set parent's left child to new node

    def insertRight(self, newNode: int = None):
        """Insert new node to the right

        Arguments:
            newNode {int} -- value of new node (default: {None})
        """
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            """if right child is not empty, new node will be inserted
            to the right of current node and right child
            """
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        """Get left child

        Returns:
            BinaryTree -- left node
        """
        return self.left

    def getRightChild(self):
        """Get right child

        Returns:
            BinaryTree -- right node
        """
        return self.right

    def getValue(self):
        """get node's value

        Returns:
            int -- node's value
        """
        return self.value

    def setValue(self, value: int):
        """set node's value

        Arguments:
            value {int} -- node's value
        """
        self.value = value

    def print(self):
        """Visualize the tree"""
        nodes = [0] + BinaryTree.BFS(self)
        depth = ceil(log(len(nodes), 2))

        for i in range(depth):
            nodesSameDepth = nodes[2**i : 2 ** (i + 1)]
            string = ", ".join("({:d})".format(node) for node in nodesSameDepth)

            print(string)

    @staticmethod
    def BFS(tree):
        """Traverse the tree horizontally

        Returns:
            list -- list of nodes
        """
        queue = []
        result = []

        queue.append(tree)

        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.getValue())

            if node.getLeftChild() is not None:
                queue.append(node.getLeftChild())
            if node.getRightChild() is not None:
                queue.append(node.getRightChild())

        return result


tree = BinaryTree(2)
tree.insertLeft(1)
tree.insertRight(3)
tree.getLeftChild().insertLeft(0)
tree.getLeftChild().insertRight(7)
tree.getRightChild().insertLeft(9)
tree.getRightChild().insertRight(1)
tree.print()
