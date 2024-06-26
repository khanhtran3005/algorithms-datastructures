def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)


def quickSortHelper(array, first, last):
    if first < last:
        splitPoint = partitioning(array, first, last)
        quickSortHelper(array, first, splitPoint - 1)
        quickSortHelper(array, splitPoint + 1, last)


def partitioning(array, first, last):
    pivot = array[first]
    left = first + 1
    right = last
    isFinished = False

    while not isFinished:
        while array[left] <= pivot and left <= right:
            left += 1

        while array[right] >= pivot and left <= right:
            right -= 1

        if left > right:
            isFinished = True
        else:
            array[left], array[right] = array[right], array[left]

    array[first], array[right] = array[right], array[first]

    return right


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
