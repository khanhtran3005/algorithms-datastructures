from classes.binarytree import BinaryTree

def find_path_to_a_node(node, number, stack=[]):
	stack = []

	if not helper(node, number, stack):
		print('Could not find node: ' + str(number))
	else:
		print('->'.join([str(i) for i in stack]))

def helper(node, number, stack=[]):
	if node == None:
		return False

	stack.append(node.getRootVal())

	if node.getRootVal() == number:
		return True

	if helper(node.getLeftChild(), number, stack) \
		or helper(node.getRightChild(), number, stack):
		return True

	stack.pop()

	return False


tree = BinaryTree(1)
tree.insertLeft(2)
tree.insertRight(3)
tree.getLeftChild().insertLeft(4)
tree.getLeftChild().insertRight(5)
tree.getRightChild().insertRight(6)

find_path_to_a_node(tree, 6)