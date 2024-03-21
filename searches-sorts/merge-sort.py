from numpy import random


def mergeSort(array):
    length = len(array)
    if length >= 2:
        mid = length // 2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                array[k] = leftHalf[i]
                i += 1
            else:
                array[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            array[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            array[k] = rightHalf[j]
            j += 1
            k += 1

    return array


array = random.randint(0, 1000, size=10).tolist()
print(mergeSort(array))
