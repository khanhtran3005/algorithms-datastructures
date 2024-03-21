def miniMaxSum(arr):
    _sum = sum(arr)
    length = len(arr)
    min = max = 0
    for i in range(length):
        temp = _sum - arr[i]
        if i == 0:
            min = max = temp

        if temp > max:
            max = temp
        if temp < min:
            min = temp

    print(min, max)


miniMaxSum([1, 2, 3, 4, 5])
