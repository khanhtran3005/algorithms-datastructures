class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        super(TreeNode, self).__init__()
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return self.value

    def __iter__(self):
        if self.hasLeftChild():
            for elem in self.left:
                yield elem

        yield self.key, self.value

        if self.hasRightChild():
            for elem in self.right:
                yield elem

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.left or self.right)

    def hasAnyChildren(self):
        return self.left or self.right

    def hasBothChildren(self):
        return self.left and self.right

    def replaceNodeData(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

        # in case of chaning left or right child
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasLeftChild():
            if self.isLeftChild():
                self.parent.left = self.left
            else:
                self.parent.right = self.left
            self.left.parent = self.parent
        elif self.hasRightChild():
            if self.isLeftChild():
                self.parent.left = self.right
            else:
                self.parent.right = self.right
            self.right.parent = self.parent
