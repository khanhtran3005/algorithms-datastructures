class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def __str__(self):
        return str(self.heapList[1:])

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

          i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.currentSize: # kiem tra xem con node leaf hay khong
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    # compare left and right
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize: # only left node exist
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]: # check whether left < right or not
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def printTree(self):
        from math import ceil
        i = 1
        while i <= ceil(self.currentSize**(1/2)):
            print(self.heapList[2**(i-1):2**i])
            i += 1
