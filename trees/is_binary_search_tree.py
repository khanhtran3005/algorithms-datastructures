def isValidBST(tree):

    if tree.hasLeftChild():
        if tree.getRootValue() < tree.getLeftChild().getRootValue():
            return False

        return isValidBST(tree.getLeftChild())
    if tree.hasRightChild():
        if tree.getRootValue() > tree.getRightChild.getRootValue():
            return False

        return isValidBST(tree.getRightChild())

    return True
