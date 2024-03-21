def binarySearch(array, item):
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = (first + last) // 2

        if array[mid] == item:
            return mid
        elif array[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return -1


def recursiveBinarySearch(array, item):
    return recursiveBinarySearchHelper(array, 0, len(array) - 1, item)


def recursiveBinarySearchHelper(array, first, last, item):
    if first < last:
        mid = (first + last) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            return recursiveBinarySearchHelper(array, mid + 1, last, item)
        else:
            return recursiveBinarySearchHelper(array, first, mid - 1, item)

    return -1


testlist = [
    0,
    1,
    2,
    8,
    13,
    17,
    19,
    32,
    42,
]

print(recursiveBinarySearch(testlist, 3))
print(recursiveBinarySearch(testlist, 19))

print(binarySearch(testlist, 3))
print(binarySearch(testlist, 19))
