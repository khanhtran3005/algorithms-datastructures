def findKthMax(array, k):
    length = len(array)
    for i in range(0, k):
        maxPos = i

        for j in range(i + 1, length):
            if array[j] > array[maxPos]:
                maxPos = j

        if maxPos != i:
            array[i], array[maxPos] = array[maxPos], array[i]

    return array[:k]


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

# print(selectionSort(array))
print(findKthMax(array, 2))
