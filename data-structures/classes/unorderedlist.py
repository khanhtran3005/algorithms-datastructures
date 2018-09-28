from node import Node

class UnorderedList():
    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, value):
        temp = Node(value)
        temp.setNext(self._head)
        self._head = temp

    def size(self):
        return self._size

    def increaseSize(self):
        self._size += 1

    def decreaseSize(self):
        self._size -= 1

    def isEmpty(self):
        return self._head == None

    def search(self, item):
        current = self._head
        index = 0

        while current != None:
            if current.getData() == item:
                return index # found index

            index += 1
            current = current.getNext()

        return -1 # not found

    def remove(self, item):
        current = self._head
        prev = None

        while current != None:
            if current.getData() == item:
                if prev != None:
                    prev.setNext(current.getNext())
                    current.setNext(Node)
                else:
                    self._head = current.getNext()

                self.decreaseSize()
                return current

            prev = current
            current = current.getNext()

        return None

    def insert(self, pos, node: Node):
        # index = 0
        current = self._head
        prev = None

        if pos > self.size():
            raise IndexError('Index out of range')

        if pos == 0:
            self._head = node
            node.setNext(current)
        else:
            for i in range(pos):
                prev = current
                current = current.getNext()

            prev.setNext(node)
            node.setNext(current)

        self.increaseSize()

    def pop(self):
        size = self.size()
        prev = self[size - 2]
        current = self[size - 1]

        prev.setNext(None)
        self.decreaseSize()
        return current



    def __str__(self):
        current = self._head
        array = []
        while current != None:
            array.append(current.getData())
            current = current.getNext()
        string = '-'.join(str(x) for x in array)
        return string

    def __getitem__(self, key):
        if key > self.size():
            raise IndexError('Index out of range')

        current = self._head
        for i in range(key):
            current = current.getNext()

        return current



mylist = UnorderedList()


mylist.add(31)
mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

# print(mylist.size())
# print(mylist.search(26))
# mylist.remove(54)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())

mylist.insert(0, Node(30))
print(mylist)
mylist.insert(1, Node(1))
mylist.insert(1, Node(13))
print(mylist)

print(mylist.pop())
print(mylist)