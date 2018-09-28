from classes.binarytree import BinaryTree
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

def buildParseTree(exp):
    tree = BinaryTree('')
    stack = []
    stack.append(tree)
    currentTree = tree
    exp = exp.split( )
    for i in exp:
        if i == '(':
            currentTree.insertLeft('')
            stack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            currentTree = stack.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.insertRight('')
            currentTree.setRootVal(i)
            stack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())

def inOrder(tree):
  if tree != None:
      inOrder(tree.getLeftChild())
      print(tree.getRootVal())
      inOrder(tree.getRightChild())

def printExp(tree):
    string = ""
    if tree:
        if (tree.getLeftChild()): string += '('

        string += printExp(tree.getLeftChild())
        string += tree.getRootVal()
        string += printExp(tree.getRightChild())

        if (tree.getRightChild()): string += ')'

    return string

pt = buildParseTree("( ( ( 10 + 5 ) + 2 ) * 3 )")
postOrder(pt)
# inOrder(pt)
# print(printExp(pt))
# print(evaluate(pt))


