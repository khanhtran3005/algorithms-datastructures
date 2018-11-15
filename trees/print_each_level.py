from classes.binarytree import BinaryTree

def printEachTreeLevel(tree):
	queue = []

	queue.append(tree)

	while queue:
		numberOfNodes = len(queue)
		nodesSameLevel = []

		while numberOfNodes > 0:
			node = queue.pop(0)
			nodesSameLevel.append(node)

			if node.getLeftChild():
				queue.append(node.getLeftChild())
			if node.getRightChild():
				queue.append(node.getRightChild())

			numberOfNodes -= 1

		print(printNodesByLevel(nodesSameLevel))

def printNodesByLevel(nodes):
	values = []
	for node in nodes:
		values.append(node.getRootVal())

	return ' '.join('({:d})'.format(x) for x in values)


tree = BinaryTree(1)
tree.insertLeft(2)
tree.insertRight(3)
tree.getLeftChild().insertLeft(4)
tree.getLeftChild().insertRight(5)
tree.getRightChild().insertRight(6)

printEachTreeLevel(tree)