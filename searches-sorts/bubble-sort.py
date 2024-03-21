def bubbleSort(array):
    isSwapped = True
    length = len(array)
    while isSwapped:
        isSwapped = False
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwapped = True
    return array


# alist=[20,30,40,90,50,60,70,80,100,110]
# alist=[54,26,93,17,77,31,44,55,20]
alist = [1, 2, 3, 4, 5]
print(bubbleSort(alist))
