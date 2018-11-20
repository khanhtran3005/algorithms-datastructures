from classes.binarytree import BinaryTree


class TreeTraversal():
    def __init__(self):
        self.tree = None

    def _toString(self, orderName, array):
        print(orderName + ': \t', ' '.join([str(x) for x in array]))


    def preorder(self):
        result = self._preOrderHelper(self.tree)
        self._toString('Pre Order', result)

    def _preOrderHelper(self, tree, result=[]):
        if tree:
            result.append(tree.getRootVal())
            self._preOrderHelper(tree.getLeftChild())
            self._preOrderHelper(tree.getRightChild())

        return result


    def inorder(self):
        result = self._inorderHelper(self.tree)
        self._toString('In Order', result)

    def _inorderHelper(self, tree, result=[]):
        if tree:
            self._inorderHelper(tree.getLeftChild())
            result.append(tree.getRootVal())
            self._inorderHelper(tree.getRightChild())

        return result


    def postorder(self):
        result = self._postorderHelper(self.tree)
        self._toString('Post Order', result)

    def _postorderHelper(self, tree, result=[]):
        if tree:
            self._postorderHelper(tree.getLeftChild())
            self._postorderHelper(tree.getRightChild())
            result.append(tree.getRootVal())

        return result


    def levelorder(self):
        result = self._levelorderHelper(self.tree)

        self._toString('Level Order', result)

    def _levelorderHelper(self, tree, queue=[]):
        queue.append(tree)
        index = 0

        while index < len(queue):
            tree = queue[index]

            if tree.getLeftChild():
                queue.append(tree.getLeftChild())

            if tree.getRightChild():
                queue.append(tree.getRightChild())

            index += 1

        return [tree.getRootVal() for tree in queue]


    def _levelorderHelperRecursive(self, queue=[], index=0):
        """ Recursive solution
        """

        if index == len(queue):
            return [node.getRootVal() for node in queue]

        tree = queue[index]
        if tree.getLeftChild():
            queue.append(tree.getLeftChild())
        if tree.getRightChild():
            queue.append(tree.getRightChild())

        return self._levelorderHelper(queue, index + 1)



class Pre_In_Construction(TreeTraversal):

    def __init__(self, preorder, inorder):
        super().__init__()

        self.pIndex = 0
        self._preorder = preorder
        self._inorder = inorder

    def construct(self):
        self.tree = self._constructHelper(0, len(self._preorder) - 1)


    def _constructHelper(self, iStart, iEnd):

        if iStart > iEnd:
            return None

        root = BinaryTree(self._preorder[self.pIndex])

        self.pIndex += 1

        if iStart == iEnd:
            return root

        inIndex = self._inorder.index(root.getRootVal())


        root.setLeftChild(self._constructHelper(iStart, inIndex - 1))
        root.setRightChild(self._constructHelper(inIndex + 1, iEnd))
        return root


class In_Post_Construction(TreeTraversal):
    def __init__(self, inorder, postorder):
        super().__init__()
        self.pIndex = len(postorder) - 1
        self._inorder = inorder
        self._postorder = postorder

    def construct(self):
        self.tree = self._constructHelper(0, self.pIndex)

    def _constructHelper(self, iStart, iEnd):
        if iEnd < iStart:
            return None

        root = BinaryTree(self._postorder[self.pIndex])
        self.pIndex -= 1

        if iStart == iEnd:
            return root

        inIndex = self._inorder.index(root.getRootVal())

        root.setRightChild(self._constructHelper(inIndex + 1, iEnd))
        root.setLeftChild(self._constructHelper(iStart, inIndex - 1))

        return root

class Pre_Post_Construction(TreeTraversal):
    """Construct a tree from pre & post order traversals

    We can only construct a tree when it is a full binary tree

    Extends:
        TreeTraversal
    """


    def __init__(self, preorder, postorder):
        super().__init__()
        self.pIndex = 0
        self._preorder = preorder
        self._postorder = postorder

    def construct(self):
        self.tree = self._constructHelper(0, len(self._preorder) - 1)

    def _constructHelper(self, iStart, iEnd):

        if iStart > iEnd:
            return None

        root = BinaryTree(self._preorder[self.pIndex])
        self.pIndex += 1

        if iStart == iEnd:
            return root

        preIndex = self._postorder.index(self._preorder[self.pIndex])

        root.setLeftChild(self._constructHelper(iStart, preIndex))
        root.setRightChild(self._constructHelper(preIndex + 1, iEnd - 1))

        return root


class Lev_In_Construction(TreeTraversal):

    def __init__(self, levelorder, inorder):
        self._levelorder = levelorder
        self._inorder = inorder

    def _getSubList(self, levelorder, inorder):
        result = []
        for i in levelorder:
            if i in inorder:
                result.append(i)

        return result

    def construct(self):
        self.tree = self._constructHelper(self._levelorder, self._inorder)

    def _constructHelper(self, levelorder, inorder):

        if not levelorder:
            return None

        root = BinaryTree(levelorder[0])

        if len(levelorder) == 1:
            return root

        inIndex = inorder.index(root.getRootVal())

        left = inorder[:inIndex]
        right = inorder[inIndex+1:]

        root.setLeftChild(self._constructHelper(self._getSubList(levelorder, left), left))
        root.setRightChild(self._constructHelper(self._getSubList(levelorder, right), right))

        return root




PREORDER    = [1,2,4,5,3,6]
POSTORDER   = [4,5,2,6,3,1]
INORDER     = [4,2,5,1,3,6]
LEVELORDER  = [1,2,3,4,5,6]


########## Full Binary Tree ##########
# PREORDER    = [1,2,4,5,3,6,7]
# INORDER     = [4,2,5,1,6,3,7]
# POSTORDER   = [4,5,2,6,7,3,1]
# LEVELORDER  = [1,2,3,4,5,6,7]


# tree = Pre_In_Construction(PREORDER, INORDER)
# tree.construct()
# tree.preorder()
# tree.inorder()


# tree = In_Post_Construction(INORDER, POSTORDER)
# tree.construct()
# tree.inorder()
# tree.postorder()

# tree = Pre_Post_Construction(PREORDER, POSTORDER)
# tree.construct()
# tree.preorder()
# tree.postorder()

tree = Lev_In_Construction(LEVELORDER, INORDER)
tree.construct()
tree.levelorder()
tree.inorder()