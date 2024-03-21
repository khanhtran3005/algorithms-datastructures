def findAnOrphanNumber(arr):
    result = 0
    for i in arr:
        result ^= i

    return result


print(findAnOrphanNumber([1, 1, 2, 2, 3]))
