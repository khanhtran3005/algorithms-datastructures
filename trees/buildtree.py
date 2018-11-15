from classes.binarytree import BinaryTree

class BuildTree():

	def __init__(self):
		self.pIndex = 0

	def buildtree(self, preorder, inorder):
		return self.buildtreeHelper(preorder, inorder, 0, len(preorder) - 1)

	def buildtreeHelper(self, preorder, inorder, iStart, iEnd):
		print('pIndex', self.pIndex)
		print('start', iStart, 'end', iEnd)

		if iStart > iEnd:
			return None
		root = BinaryTree(preorder[self.pIndex])
		
		print('root', root.getRootVal())
		print('-----------')
		
		self.pIndex += 1

		if iStart == iEnd:
			return root

		inIndex = inorder.index(root.getRootVal())

		root.setLeftChild(self.buildtreeHelper(preorder, inorder, iStart, inIndex - 1))
		root.setRightChild(self.buildtreeHelper(preorder, inorder, inIndex + 1, iEnd))
		return root


def preorder(tree):
    # print root node first
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

tree = BuildTree().buildtree([1,2,4,5,3,6], [4,2,5,1,3,6])

preorder(tree)