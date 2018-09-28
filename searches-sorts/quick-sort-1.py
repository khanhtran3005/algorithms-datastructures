from numpy import random

def quickSort(array, first, last):

    if last > first:
        pivot = array[first]
        left = first + 1
        right = last
        isFinished = False

        while not isFinished:
            while left <= right and array[left] <= pivot:
                left += 1

            while left <= right and array[right] >= pivot:
                right -= 1

            if left > right:
                isFinished = True
            else:
                array[left], array[right] = swap(array[left], array[right])


        array[first], array[right] = swap(array[first], array[right])

        splitpoint = right

        quickSort(array, first, splitpoint - 1)
        quickSort(array, splitpoint + 1, last)

    return array


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

array = random.randint(0, 1000, size=10).tolist()

print(quickSort(array, 0, len(array) - 1))