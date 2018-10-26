def selectionSort(array):
    length = len(array)
    for i in range(0, length-1):
        minPos = i

        for j in range(i+1, length):
            if array[j] < array[minPos]:
                minPos = j

        if minPos != i:
            array[i], array[minPos] = array[minPos], array[i]

    return array

array = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(selectionSort(array))