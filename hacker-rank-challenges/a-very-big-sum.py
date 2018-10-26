def aVeryBigSum(ar):
    if len(ar) > 1:
        return ar[0] + aVeryBigSum(ar[1:len(ar)])
    else:
        return ar[0]

a = [2, 3, 4, 5]

print(aVeryBigSum(a))