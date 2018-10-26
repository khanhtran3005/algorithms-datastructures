def birthdayCakeCandles(arr):
    length = len(arr)
    max = 0
    count = 0

    for i in range(length):
        if arr[i] > max:
            max = arr[i]
            count = 1
        elif arr[i] == max:
            count += 1

    print(count)

birthdayCakeCandles([3,2,1,3])