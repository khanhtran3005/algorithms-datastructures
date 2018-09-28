from classes.binarysearchtree import BinarySearchTree

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

# print(mytree[6])
# print(mytree[2])

del mytree[3]
# print(mytree[2])
# print(mytree.length())

for k, v in mytree:
    print(k, v)