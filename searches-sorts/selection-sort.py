def selectionSort(array):
    length = len(array)
    for i in range(0, length-1):
        minPos = i

        for j in range(i+1, length):
            if array[j] < array[minPos]:
                minPos = j

        if minPos != i:
            array[i], array[minPos] = swap(array[i], array[minPos])

    return array

def findMaxKth(array, k):
    length = len(array)
    for i in range(0, k):
        maxPos = i

        for j in range(i+1, length):
            if array[j] > array[maxPos]:
                maxPos = j

        if maxPos != i:
            array[i], array[maxPos] = swap(array[i], array[maxPos])

    return array[:k]

def find2Max(array):
    firstMax = second
    for i in array:



def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

array = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

# print(selectionSort(array))
print(findMaxKth(array, 2))