def diagonalDifference(arr):
    ltr = rtl = 0
    length = len(arr)
    for i in range(length):
        ltr += arr[i][i]
        rtl += arr[length - 1 - i][i]

    return abs(ltr - rtl)

a = [[1,2,3], [4,5,6], [7,8,9]]

print(diagonalDifference(a))