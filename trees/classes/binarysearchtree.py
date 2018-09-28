from .treenode import TreeNode

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._get(key,self.root))

    def __delitem__(self,key):
        self.delete(key)

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

        self.size += 1

    def _put(self, key, value, currentNode):
        if currentNode.key > key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.hasLeftChild())
            else:
                currentNode.left = TreeNode(key, value, parent=currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.hasRightChild())
            else:
                currentNode.right = TreeNode(key, value, parent=currentNode)

    def get(self, key):
        if not self.root: return None

        return self._get(key, self.root)

    def _get(self, key, currentNode):
        if not currentNode: return None

        if currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.hasLeftChild())
        else:
            return self._get(key, currentNode.hasRightChild())

    def delete(self, key):
        if self.size == 0:
            raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
        else:
            node = self.get(key)
            if node.isLeaf():
                self.deleteLeafNode(node)
            elif node.hasBothChildren():
                self.deleteHasBothChildren(node)
            else:
                self.deleteHasOneChild(node)
        self.size -= 1

    def deleteLeafNode(self, currentNode):
        if currentNode == currentNode.parent.left:
            currentNode.parent.left = None
        else:
            currentNode.parent.right = None

    def deleteHasOneChild(self, currentNode):
        if currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.left.parent = currentNode.parent
                currentNode.parent.left = currentNode.left
            elif currentNode.isRightChild():
                currentNode.left.parent = currentNode.parent
                currentNode.parent.right = currentNode.left
            else: # root case
                leftChild = currentNode.left
                currentNode.replaceNodeData(leftChild.key, leftChild.value, leftChild.left, leftChild.right, leftChild.parent)
        else:
            if currentNode.isLeftChild():
                currentNode.parent.left = currentNode.right
                currentNode.right.parent = currentNode.parent
            elif currentNode.isRightChild():
                currentNode.parent.right = currentNode.right
                currentNode.right.parent = currentNode.parent
            else:
                rightChild = currentNode.right
                currentNode.replaceNodeData(rightChild.key, rightChild.value, rightChild.left, rightChild.right, rightChild.parent)

    def deleteHasBothChildren(self, currentNode):
        successor = self.findMin(currentNode)
        successor.spliceOut()
        currentNode.key = successor.key
        currentNode.value = successor.value


    def findMin(self, currentNode):
        if not currentNode.left:
            return currentNode

        return self.findMin(currentNode.left)




