def sansaXor(arr):
    length = len(arr)
    xor = 0
    i = 0
    if length % 2 == 0:
        return 0

    while i < length:
        # print(arr[i])
        xor ^= arr[i]
        i += 2
    return xor


print(sansaXor([4, 5, 7, 5]))
