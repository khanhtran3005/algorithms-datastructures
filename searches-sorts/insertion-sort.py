def insertionSort(array):
    length = len(array)
    for i in range(1, length):
        currentValue = array[i]
        position = i

        for j in range(i - 1, -1, -1):
            if array[j] <= currentValue:
                break

            array[j + 1] = array[j]
            position = j

        if position != i:
            array[position] = currentValue
    return array


array = [
    3,
    44,
    38,
    5,
    47,
    15,
    36,
    26,
    27,
    2,
    46,
    4,
    19,
    50,
    48,
    3,
    44,
    38,
    5,
    47,
    15,
    36,
    26,
    27,
    2,
    46,
    4,
    19,
    50,
    48,
    3,
    44,
    38,
    5,
    47,
    15,
    36,
    26,
    27,
    2,
    46,
    4,
    19,
    50,
    48,
]
print(insertionSort(array))
